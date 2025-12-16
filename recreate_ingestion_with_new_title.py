#!/usr/bin/env python3
"""
MinIO에 저장된 문서를 다운로드 없이 복사하여 제목 변경 후 Ingestion 작업 생성 스크립트

기존 데이터는 삭제하지 않고, 새로운 제목으로 별도 문서로 처리합니다.
MinIO의 copy_object 기능을 사용하여 파일을 다운로드하지 않고 복사합니다.

사용법:
    python recreate_ingestion_with_new_title.py <minio_path> --service-id SERVICE_ID [옵션]
    
예시:
    python recreate_ingestion_with_new_title.py "minio:interview/2025/01/15/document.pdf" \\
        --service-id interview \\
        --minio-endpoint remote-server.com:9000 \\
        --minio-access-key YOUR_KEY \\
        --minio-secret-key YOUR_SECRET \\
        --suffix "_reupload"
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime
import requests
from typing import Optional
import uuid

# 프로젝트 루트를 Python 경로에 추가
script_dir = Path(__file__).parent
backend_dir = script_dir.parent
sys.path.insert(0, str(backend_dir))

from minio import Minio
from minio.error import S3Error
from minio.commonconfig import CopySource
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()


def get_minio_client(
    endpoint: Optional[str] = None,
    host: Optional[str] = None,
    port: Optional[int] = None,
    access_key: Optional[str] = None,
    secret_key: Optional[str] = None,
    secure: Optional[bool] = None
):
    """
    MinIO 클라이언트 생성
    
    Args:
        endpoint: MinIO 서버 엔드포인트 (예: remote-server.com:9000)
        host: MinIO 서버 호스트 (endpoint보다 우선)
        port: MinIO 서버 포트 (endpoint보다 우선)
        access_key: MinIO 액세스 키
        secret_key: MinIO 시크릿 키
        secure: HTTPS 사용 여부 (기본값: False)
    """
    # 명령줄 인자가 없으면 환경 변수에서 가져오기
    access_key = access_key or os.getenv("MINIO_ROOT_USER")
    secret_key = secret_key or os.getenv("MINIO_ROOT_PASSWORD")
    
    if secure is None:
        secure_env = os.getenv("MINIO_SECURE", "false").lower()
        secure = secure_env == "true"
    
    # host와 port가 모두 제공되면 그것을 우선 사용
    if host and port:
        endpoint = f"{host}:{port}"
    elif host:
        # host만 제공되면 기본 포트 사용
        default_port = 9000 if not secure else 9000
        endpoint = f"{host}:{default_port}"
    else:
        # endpoint 사용
        endpoint = endpoint or os.getenv("MINIO_ENDPOINT")
    
    if not endpoint:
        raise ValueError(
            "MinIO 엔드포인트가 설정되지 않았습니다. "
            "--minio-endpoint 또는 --minio-host/--minio-port 인자를 설정하세요."
        )
    if not access_key:
        raise ValueError(
            "MinIO 액세스 키가 설정되지 않았습니다. "
            "--minio-access-key 인자 또는 MINIO_ROOT_USER 환경 변수를 설정하세요."
        )
    if not secret_key:
        raise ValueError(
            "MinIO 시크릿 키가 설정되지 않았습니다. "
            "--minio-secret-key 인자 또는 MINIO_ROOT_PASSWORD 환경 변수를 설정하세요."
        )
    
    return Minio(
        endpoint=endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=secure,
    )


def parse_minio_path(minio_path: str) -> tuple[str, str, str]:
    """
    minio: 경로를 파싱하여 오브젝트 키, 파일명, 서비스 ID 반환
    
    Args:
        minio_path: "minio:service_id/YYYY/MM/DD/filename" 형식의 경로
        
    Returns:
        (object_key, filename, service_id) 튜플
    """
    if not minio_path.startswith("minio:"):
        raise ValueError(f"경로는 'minio:'로 시작해야 합니다: {minio_path}")
    
    # "minio:" 접두사 제거
    object_key = minio_path[6:]
    
    # 파일명 추출
    filename = Path(object_key).name
    
    # 서비스 ID 추출 (첫 번째 경로 세그먼트)
    parts = object_key.split("/")
    service_id = parts[0] if parts else None
    
    return object_key, filename, service_id


def generate_new_path(object_key: str, new_filename: str) -> str:
    """
    새로운 오브젝트 키 생성 (파일명만 변경)
    
    Args:
        object_key: 기존 오브젝트 키
        new_filename: 새로운 파일명
        
    Returns:
        새로운 오브젝트 키
    """
    path = Path(object_key)
    # 디렉토리 부분은 유지하고 파일명만 변경
    new_path = path.parent / new_filename
    return str(new_path)


def rename_file_for_reupload(original_filename: str, suffix: Optional[str] = None) -> str:
    """
    중복 방지를 위해 파일명 변경
    
    Args:
        original_filename: 원본 파일명
        suffix: 추가할 접미사 (없으면 타임스탬프 사용)
        
    Returns:
        변경된 파일명
    """
    path = Path(original_filename)
    stem = path.stem
    ext = path.suffix
    
    if suffix:
        new_stem = f"{stem}{suffix}"
    else:
        # 타임스탬프 추가
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_stem = f"{stem}_{timestamp}"
    
    return f"{new_stem}{ext}"


def copy_file_in_minio(
    client: Minio,
    bucket_name: str,
    source_object_key: str,
    dest_object_key: str
) -> bool:
    """
    MinIO에서 파일을 복사 (다운로드 없이)
    
    Args:
        client: MinIO 클라이언트
        bucket_name: 버킷 이름
        source_object_key: 원본 오브젝트 키
        dest_object_key: 대상 오브젝트 키
        
    Returns:
        복사 성공 여부
    """
    print(f"📋 MinIO에서 파일 복사 중...")
    print(f"   버킷: {bucket_name}")
    print(f"   원본: {source_object_key}")
    print(f"   대상: {dest_object_key}")
    
    try:
        # CopySource 생성
        copy_source = CopySource(bucket_name, source_object_key)
        
        # 파일 복사
        client.copy_object(
            bucket_name,
            dest_object_key,
            copy_source
        )
        
        print(f"✅ 파일 복사 완료!")
        return True
        
    except S3Error as e:
        print(f"❌ 파일 복사 실패: {e}")
        return False


def create_ingestion_job(
    file_path: str,
    api_base_url: Optional[str] = None,
    auth_token: Optional[str] = None,
    make_ontology: bool = False,
    metadata: Optional[dict] = None
) -> dict:
    """
    Ingestion 작업 생성
    
    Args:
        file_path: 처리할 파일 경로 (minio: 형식)
        api_base_url: API 기본 URL
        auth_token: 인증 토큰 (선택사항)
        make_ontology: 온톨로지 생성 여부
        metadata: 추가 메타데이터
        
    Returns:
        작업 생성 응답
    """
    if api_base_url is None:
        api_base_url = os.getenv("API_BASE_URL", "http://localhost:8000")
    
    ingestion_url = f"{api_base_url}/api/v1/ingestions/"
    
    print(f"🔄 Ingestion 작업 생성 중...")
    print(f"   URL: {ingestion_url}")
    print(f"   파일 경로: {file_path}")
    
    try:
        # Idempotency-Key 생성 (파일 경로 기반)
        idempotency_key = f"recreate-{uuid.uuid4()}"
        
        headers = {
            'Content-Type': 'application/json',
            'Idempotency-Key': idempotency_key,
        }
        if auth_token:
            headers['Authorization'] = f"Bearer {auth_token}"
        
        payload = {
            "file_paths": [file_path],
            "make_ontology": make_ontology,
            "metadata": {
                **(metadata or {}),
                "created_from": "recreate_script",
                "recreated_at": datetime.now().isoformat(),
            }
        }
        
        # retry_timestamp를 포함하지 않아서 기존 작업 삭제 안 함
        response = requests.post(ingestion_url, json=payload, headers=headers, timeout=300)
        response.raise_for_status()
        
        result = response.json()
        print(f"✅ Ingestion 작업 생성 완료!")
        print(f"   작업 수: {result.get('total_jobs', 0)}")
        
        if result.get('jobs'):
            for job in result['jobs']:
                print(f"   - Job UUID: {job.get('job_uuid')}")
                print(f"     상태: {job.get('status')}")
                print(f"     위치: {job.get('location', 'N/A')}")
        
        return {"success": True, "response": result}
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Ingestion 작업 생성 실패: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"   응답 내용: {e.response.text}")
        return {"success": False, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(
        description="MinIO 문서를 다운로드 없이 복사하여 제목 변경 후 Ingestion 작업 생성",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  # 기본 사용 (타임스탬프로 파일명 변경) - endpoint 방식
  python recreate_ingestion_with_new_title.py "minio:interview/2025/01/15/document.pdf" \\
    --service-id interview \\
    --minio-endpoint remote-server.com:9000 \\
    --minio-access-key YOUR_KEY \\
    --minio-secret-key YOUR_SECRET

  # host와 port 분리 방식
  python recreate_ingestion_with_new_title.py "minio:interview/2025/01/15/document.pdf" \\
    --service-id interview \\
    --minio-host remote-server.com \\
    --minio-port 9000 \\
    --minio-access-key YOUR_KEY \\
    --minio-secret-key YOUR_SECRET

  # 커스텀 접미사 사용
  python recreate_ingestion_with_new_title.py "minio:interview/2025/01/15/document.pdf" \\
    --service-id interview \\
    --minio-host remote-server.com \\
    --minio-port 9000 \\
    --minio-access-key YOUR_KEY \\
    --minio-secret-key YOUR_SECRET \\
    --suffix "_backup"

  # 온톨로지 생성 포함
  python recreate_ingestion_with_new_title.py "minio:interview/2025/01/15/document.pdf" \\
    --service-id interview \\
    --minio-host remote-server.com \\
    --minio-port 9000 \\
    --minio-access-key YOUR_KEY \\
    --minio-secret-key YOUR_SECRET \\
    --make-ontology
        """
    )
    
    parser.add_argument(
        "minio_path",
        help="MinIO 경로 (예: minio:interview/2025/01/15/document.pdf)"
    )
    parser.add_argument(
        "--service-id",
        required=True,
        help="서비스 ID (업로드할 서비스)"
    )
    parser.add_argument(
        "--suffix",
        help="파일명에 추가할 접미사 (없으면 타임스탬프 자동 추가)"
    )
    parser.add_argument(
        "--bucket-name",
        default=None,
        help="MinIO 버킷 이름 (기본값: MINIO_BUCKET_NAME 환경 변수 또는 'gorag-files')"
    )
    parser.add_argument(
        "--api-url",
        default=None,
        help="API 기본 URL (기본값: API_BASE_URL 환경 변수 또는 'http://localhost:8000')"
    )
    parser.add_argument(
        "--auth-token",
        default=None,
        help="인증 토큰 (선택사항)"
    )
    parser.add_argument(
        "--minio-endpoint",
        default=None,
        help="MinIO 서버 엔드포인트 (예: remote-server.com:9000, 기본값: MINIO_ENDPOINT 환경 변수)"
    )
    parser.add_argument(
        "--minio-host",
        default=None,
        help="MinIO 서버 호스트 (--minio-endpoint보다 우선, --minio-port와 함께 사용)"
    )
    parser.add_argument(
        "--minio-port",
        type=int,
        default=None,
        help="MinIO 서버 포트 (--minio-endpoint보다 우선, --minio-host와 함께 사용, 기본값: 9000)"
    )
    parser.add_argument(
        "--minio-access-key",
        default=None,
        help="MinIO 액세스 키 (기본값: MINIO_ROOT_USER 환경 변수)"
    )
    parser.add_argument(
        "--minio-secret-key",
        default=None,
        help="MinIO 시크릿 키 (기본값: MINIO_ROOT_PASSWORD 환경 변수)"
    )
    parser.add_argument(
        "--minio-secure",
        action="store_true",
        help="MinIO HTTPS 사용 (기본값: False)"
    )
    parser.add_argument(
        "--make-ontology",
        action="store_true",
        help="온톨로지 생성 여부 (기본값: False)"
    )
    
    args = parser.parse_args()
    
    # 버킷 이름 결정
    bucket_name = args.bucket_name or os.getenv("MINIO_BUCKET_NAME", "gorag-files")
    
    print("=" * 60)
    print("MinIO 문서 복사 + Ingestion 작업 생성 스크립트")
    print("(다운로드 없이 MinIO 내부에서 복사)")
    print("=" * 60)
    print(f"입력 경로: {args.minio_path}")
    print(f"서비스 ID: {args.service_id}")
    print(f"버킷 이름: {bucket_name}")
    print(f"온톨로지 생성: {args.make_ontology}")
    print()
    
    try:
        # 1. MinIO 경로 파싱
        object_key, original_filename, path_service_id = parse_minio_path(args.minio_path)
        print(f"📄 원본 파일명: {original_filename}")
        print(f"🔑 오브젝트 키: {object_key}")
        print(f"📁 경로의 서비스 ID: {path_service_id}")
        print()
        
        # 2. 파일명 변경
        new_filename = rename_file_for_reupload(original_filename, args.suffix)
        print(f"📝 파일명 변경: {original_filename} → {new_filename}")
        
        # 3. 새로운 경로 생성
        new_object_key = generate_new_path(object_key, new_filename)
        new_minio_path = f"minio:{new_object_key}"
        print(f"🆕 새로운 경로: {new_minio_path}")
        print()
        
        # 4. MinIO 클라이언트 생성
        client = get_minio_client(
            endpoint=args.minio_endpoint,
            host=args.minio_host,
            port=args.minio_port,
            access_key=args.minio_access_key,
            secret_key=args.minio_secret_key,
            secure=args.minio_secure
        )
        
        # 5. MinIO에서 파일 복사 (다운로드 없이)
        if not copy_file_in_minio(client, bucket_name, object_key, new_object_key):
            sys.exit(1)
        
        print()
        
        # 6. Ingestion 작업 생성
        ingestion_result = create_ingestion_job(
            file_path=new_minio_path,
            api_base_url=args.api_url,
            auth_token=args.auth_token,
            make_ontology=args.make_ontology,
            metadata={"service_id": args.service_id}
        )
        
        if not ingestion_result.get("success"):
            print("⚠️  파일 복사는 완료되었으나 Ingestion 작업 생성에 실패했습니다.")
            print("   수동으로 Ingestion 작업을 생성할 수 있습니다.")
            print(f"   파일 경로: {new_minio_path}")
            sys.exit(1)
        
        print()
        print("=" * 60)
        print("✅ 파일 복사 및 Ingestion 작업 생성 완료!")
        print("=" * 60)
        print(f"📁 새 파일 경로: {new_minio_path}")
        print("💡 기존 데이터는 유지되며, 새로운 제목으로 별도 문서로 처리됩니다.")
        print("💡 파일은 MinIO 내부에서 복사되었으므로 EDM 보안의 영향을 받지 않습니다.")
                
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()


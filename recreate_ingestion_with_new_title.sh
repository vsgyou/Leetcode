#!/bin/bash
#
# MinIO 문서를 다운로드 없이 복사하여 제목 변경 후 Ingestion 작업 생성 스크립트 (Bash 래퍼)
#
# 사용법:
#   ./recreate_ingestion_with_new_title.sh <minio_path> --service-id SERVICE_ID [옵션]
#
# 예시:
#   ./recreate_ingestion_with_new_title.sh "minio:interview/2025/01/15/document.pdf" \\
#     --service-id interview \\
#     --minio-endpoint remote-server.com:9000 \\
#     --minio-access-key YOUR_KEY \\
#     --minio-secret-key YOUR_SECRET
#

set -e  # 오류 발생 시 즉시 종료

# 스크립트 디렉토리 찾기
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# Python 스크립트 경로
PYTHON_SCRIPT="$SCRIPT_DIR/recreate_ingestion_with_new_title.py"

# Python 스크립트가 존재하는지 확인
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "❌ 오류: Python 스크립트를 찾을 수 없습니다: $PYTHON_SCRIPT"
    exit 1
fi

# Python 실행 파일 찾기
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ 오류: Python을 찾을 수 없습니다"
    exit 1
fi

# 백엔드 디렉토리로 이동
cd "$BACKEND_DIR"

# Python 스크립트 실행 (모든 인자를 전달)
echo "🚀 Python 스크립트 실행 중..."
echo ""
exec "$PYTHON_CMD" "$PYTHON_SCRIPT" "$@"


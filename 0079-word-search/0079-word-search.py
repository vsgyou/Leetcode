class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n_rows, n_cols = len(board), len(board[0])
        traserving = set()

        def dfs(row, col, idx):
            # 기저조건 1: word에서 찾을 단어를 모두 찾은 경우 TRUE 반환
            if idx == len(word):
                return True
            # 기저조건 2: 찾고있는 위치가 범위를 벗어나면 FALSE 반환
            if not (0<= row < n_rows and 0 <= col < n_cols):
                return False
            # 기저조건 3: 찾는 숫자가 없으면 FALSE 반환
            if board[row][col] != word[idx]:
                return False
            # 기저조건 4: 이미 방문했던 경로인 경우 FALSE 반환
            if (row, col) in traserving:
                return False
            
            traserving.add((row,col))
            for r, c in [(-1,0), (1,0), (0,-1), (0,1)]:
                if dfs(row + r, col + c, idx + 1):
                    return True
            traserving.remove((row,col))
        
        # 초기 위치 찾기
        for r in range(n_rows):
            for c in range(n_cols):
                if dfs(r,c,0):
                    return True
        return False
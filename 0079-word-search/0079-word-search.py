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
            if idx == len(word):
                return True
            if not (0<= row < n_rows and 0 <= col < n_cols):
                return False
            if board[row][col] != word[idx]:
                return False
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
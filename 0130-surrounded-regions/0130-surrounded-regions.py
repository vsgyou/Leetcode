class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(row,col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[row]) or board[row][col] != "O":
                return
            board[row][col] = "T"
            
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O" and (r in [0, len(board)-1] or c in [0,len(board[r]) -1]):
                    dfs(r,c)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "T":
                    board[r][c] = "O"
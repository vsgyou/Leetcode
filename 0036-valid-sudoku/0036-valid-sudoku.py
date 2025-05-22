class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        result = []
        for row in (board):
            seen = set()
            for col in row:
                if col != '.':
                    if col in seen:
                        return False
                    seen.add(col)
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for mat_row in range(3):
            for mat_col in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        r = mat_row*3 + row
                        c = mat_col*3 + col
                        if board[r][c] != '.':
                            if board[r][c] in seen:
                                return False
                            seen.add(board[r][c])
        return True
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        result = []
        for row in board:
            seen = set()
            for col in row:
                if col != ".":
                    if col in seen:
                        return False
                    seen.add(col)
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        for rows in range(3):
            for cols in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if board[rows*3+row][cols*3+col] != ".":
                            if board[rows*3+row][cols*3+col] in seen:
                                return False
                            seen.add(board[rows*3+row][cols*3+col])
        return True
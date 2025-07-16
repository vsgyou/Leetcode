class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(len(board)):
            seen = set()
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        return False

        for col in range(len(board)):
            seen = set()
            for row in range(len(board[0])):
                if board[row][col] != ".":
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        return False

        for i in range(3):
            for j in range(3):
                seen = set()
                for row in range(3):
                    for col in range(3):
                        if board[i*3+row][j*3+col] != ".":    
                            if board[i*3+row][j*3+col] not in seen:
                                seen.add(board[i*3+row][j*3+col])
                            else:
                                return False
            
        return True

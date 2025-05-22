class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        max_row = len(board)
        max_col = len(board[0])

        def num_live_count(row, col):
            count_live = 0
            idx_dict = [(-1,-1),(-1,0),(-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

            for nr, nc in idx_dict:
                dr = row + nr
                dc = col + nc
                if 0 <= dr < max_row and 0 <= dc < max_col and abs(board[dr][dc]) == 1:
                    count_live += 1
            return count_live
        
        for i in range(max_row):
            for j in range(max_col):
                num_count = num_live_count(i,j)
                if board[i][j] == 1 and (num_count < 2 or num_count > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and num_count == 3:
                    board[i][j] = 2

        for i in range(max_row):
            for j in range(max_col):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1 
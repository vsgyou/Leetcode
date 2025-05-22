from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        def get_position(cell):
            row, col = divmod(cell-1, n)
            real_row = n-1-row
            real_col = col if row % 2 == 0 else n-col-1

            return real_row, real_col

        queue = deque([(1,0)])
        visited = set()

        while queue:
            curr, moves = queue.popleft()
            if curr == n*n:
                return moves
            
            for next_pos in range(curr+1, min(curr+7, n*n+1)):
                row, col = get_position(next_pos)
                destination = board[row][col] if board[row][col] != -1 else next_pos

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves+1))

        return -1    
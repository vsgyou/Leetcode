class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        1 - 3 - 1 - 1 - 1 = 7
                5 - 1 - 1 = 11
                    2 - 1 = 12
            1 - 5 - 1 - 1 = 9
                    2 - 1 = 10
                4 - 2 - 1 = 9
        """
        if not grid and not grid[0]:
            return 0
        
        m,n = len(grid), len(grid[0])

        for row in range(1, m):
            grid[row][0] = grid[row-1][0] + grid[row][0]
        for col in range(1, n):
            grid[0][col] = grid[0][col-1] + grid[0][col]
        
        for row in range(1, m):
            for col in range(1, n):
                grid[row][col] = grid[row][col]+min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]
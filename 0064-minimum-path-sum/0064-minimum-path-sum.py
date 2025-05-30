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
        if not grid or not grid[0]:
            return 0
        m,n = len(grid), len(grid[0])

        for i in range(1 ,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]
                
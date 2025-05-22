class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # def sink(row,col):
        #     grid[row][col] = "0"

        #     for r,c in [(row+1, col), (row-1,col), (row, col+1), (row, col-1)]:
        #         if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == "1":
        #             sink(r,c)

        def sink(row, col):
            stack = [(row,col)]
            while stack:
                row, col = stack.pop()
                grid[row][col] = "0"

                for r, c in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                    if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]=="1":
                        stack.append((r,c))
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    cnt += 1
                    sink(r,c)
        
        return cnt
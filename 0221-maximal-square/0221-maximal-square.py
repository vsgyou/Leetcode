class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        width, height = len(matrix[0]), len(matrix)
        maxValue = 0
        dp = [[0] * width for _ in range(height)]

        for i in range(width):
            dp[0][i] = int(matrix[0][i])
            maxValue = max(maxValue, dp[0][i])

        for i in range(height):
            dp[i][0] = int(matrix[i][0])
            maxValue = max(maxValue, dp[i][0])

        for i in range(1, height):
            for j in range(1, width):
                dp[i][j] = int(matrix[i][j])
                if dp[i][j] == 1 and dp[i-1][j] > 0 and dp[i-1][j-1] > 0 and dp[i][j-1] >0:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                maxValue = max(maxValue, dp[i][j])

        return maxValue**2
                    


        
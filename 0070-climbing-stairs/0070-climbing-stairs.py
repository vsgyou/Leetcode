class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        
           -
          -
         -
        -
        n=1, 1가지
        n=2, 2가지 (1,1), (2)
        n=3, 1에 도착한 경우 + 2에 도착한 경우 = 3가지
        n=4, 2에 도착한 경우 + 3에 도착한 경우 = 5가지
        .
        .
        .
        f(n) = f(n-2) + f(n-1)
        """

        # dp = {1:1, 2:2}
        # for i in range(3, n+1):
        #     dp[i] = dp[i-2] + dp[i-1]
        
        # return dp[n]
        
        # 공간복잡도 개선
        if n < 3:
            return n

        pre, cur = 1, 2
        
        for _ in range(n-2):
            pre, cur = cur, cur+pre
        return cur
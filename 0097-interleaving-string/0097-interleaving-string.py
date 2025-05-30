class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        N1, N2 = len(s1), len(s2)
        if len(s3) != N1+N2:    return False
        
        dp = [[False]*(N2+1) for _ in range(N1+1)]
        dp[0][0] = True
        
        for n in range(1, N1+1):
            dp[n][0] = (s1[n-1] == s3[n-1]) and dp[n-1][0]
        
        for n in range(1, N2+1):
            dp[0][n] = (s2[n-1] == s3[n-1]) and dp[0][n-1]
        
        for n in range(1, N1+1):
            for m in range(1, N2+1):
                t1 = (s1[n-1] == s3[n+m-1]) and dp[n-1][m]
                t2 = (s2[m-1] == s3[n+m-1]) and dp[n][m-1]
                dp[n][m] = t1 or t2
                
        return dp[N1][N2]
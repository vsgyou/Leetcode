class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [True] + [False]*len(s)
        for i in range(1, len(s)+1):
            for word in wordDict:
                if s[i-len(word):i] == word:
                    dp[i] = dp[i-len(word)]
                if dp[i]:
                    break
        return dp[-1]
        
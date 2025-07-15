class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        for alpha in t:
            if start < len(s) and alpha == s[start]:
                start += 1

        return start == len(s)
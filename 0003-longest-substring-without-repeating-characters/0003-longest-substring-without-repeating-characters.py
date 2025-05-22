class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        best_len = 0 
        s_dict = {}
        for end in range(len(s)):
            if s[end] in s_dict and s_dict[s[end]] >= start:
                start = s_dict[s[end]] + 1
            s_dict[s[end]] = end
            best_len = max(best_len, end-start+1)
        return best_len
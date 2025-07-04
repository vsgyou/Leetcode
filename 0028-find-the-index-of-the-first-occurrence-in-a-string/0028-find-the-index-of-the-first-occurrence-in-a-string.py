class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        
        n = len(needle)
        result = 0
        for i in range(len(haystack)-(n-1)):
            if haystack[i:i+n] == needle:
                result = i
                break
        return result
        
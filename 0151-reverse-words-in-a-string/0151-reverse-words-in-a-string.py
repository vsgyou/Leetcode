class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strings = s.split()
        return " ".join(strings[::-1])
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered_s = "".join(char.lower() for char in s if char.isalnum())
        return filtered_s == filtered_s[::-1]
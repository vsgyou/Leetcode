class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        
        # original_x = x
        # reversed_num = 0
        # while x > 0:
        #     digit = x % 10
        #     reversed_num = reversed_num*10 + digit
        #     x = x // 10
        
        # return original_x == reversed_num

        if x < 0:
            return False
        original_x = x
        reversed_num = int(str(x)[::-1])
        
        return original_x == reversed_num
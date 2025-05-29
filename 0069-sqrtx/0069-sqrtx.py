class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # # 이진탐색 방법
        # if x == 0:
        #     return 0
        
        # left, right = 0, x

        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid < x:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return right

        # 뉴턴의 방법
        if x == 0 :
            return 0
        
        guess = x
        while guess * guess > x:
            guess = (guess + x // guess) // 2
            print(guess)
        return guess
        
        """
        x = 4, guess = 4, guess = (4 + 4 // 4) // 4 = (2) // 2 = 0
        """
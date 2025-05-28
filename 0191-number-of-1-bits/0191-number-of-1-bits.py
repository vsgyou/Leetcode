class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            output = n % 2
            if output == 1:
                count += 1
            n = n // 2
        return count
        
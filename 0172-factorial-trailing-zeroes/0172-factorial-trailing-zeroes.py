class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        
        1x2x3x4x5x6x7x8x9x10
        """

        count = 0
        while n > 0:
            n //= 5  # 5의 배수가 몇 개 있는지 확인, 5가 포함되면 2는 무조건 포함되므로
            count += n  # 현재 몫을 누적하여 0의 개수 추가
        return count

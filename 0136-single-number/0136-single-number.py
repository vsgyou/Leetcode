class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = []
        # for num in nums:
        #     if num not in result:
        #         result.append(num)
        #     else:
        #         result.remove(num)
        # return result[0]
        
        # XOR 사용
        result = 0
        for num in nums:
            result ^= num
        return result
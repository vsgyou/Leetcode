class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)

        return candidate
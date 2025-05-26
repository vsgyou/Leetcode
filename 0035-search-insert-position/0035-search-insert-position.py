class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt = 0
        for num in nums:
            if num < target:
                cnt += 1
            else:
                 break
        return cnt
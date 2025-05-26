class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if 0 < mid and nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[0]
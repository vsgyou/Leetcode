class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_jump = 0
        curr_idx = 0

        for i in range(len(nums)):
            if i > max_jump:
                return False
            max_jump = max(i+nums[i], max_jump)
        return True
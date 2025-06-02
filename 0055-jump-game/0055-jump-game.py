class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums) == 1:
        #     return True 

        max_jump = 0
        curr_idx = 0
        while curr_idx <= max_jump:
            max_jump = max(max_jump, curr_idx+nums[curr_idx])
            if max_jump >= len(nums)-1:
                return True
            curr_idx += 1
        return False
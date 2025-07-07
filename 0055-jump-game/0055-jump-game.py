class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # max_jump = 0
        # for i in range(len(nums)):
        #     if i > max_jump:
        #         return False
        #     max_jump = max(i+nums[i], max_jump)
        # return True

        max_jump = 0
        curr_idx = 0
        
        while curr_idx <= max_jump:
            max_jump = max(nums[curr_idx] + curr_idx, max_jump)
            if max_jump >= len(nums)-1:
                return True
            curr_idx += 1
        return False
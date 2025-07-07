class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_idx = 0
        max_idx = 0
        jump_count = 0

        for i in range(len(nums)-1):
            max_idx = max(i+nums[i], max_idx)
            if i == curr_idx:
                curr_idx = max_idx
                jump_count += 1
            if curr_idx >= len(nums)-1:
                break
        return jump_count
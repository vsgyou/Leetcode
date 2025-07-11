class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
                [2, 3, 1, 1, 4]
        max      2  4  4  4  4
        curr     2  2  4  4  4
        jump     1  1  2  2  2
        """
        curr_idx = 0
        max_jump = 0
        jump_count = 0

        for i in range(len(nums)-1):
            max_jump = max(i+nums[i], max_jump)
            if i == curr_idx:
                curr_idx = max_jump
                jump_count += 1
            if curr_idx >= len(nums)-1:
                break
        return jump_count
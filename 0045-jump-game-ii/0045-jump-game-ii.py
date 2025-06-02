class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jump_count = 0
        max_len = 0
        current_idx = 0
        
        for i in range(len(nums)-1):
            max_len = max(max_len, nums[i] + i)
            if i == current_idx:
                current_idx = max_len
                jump_count += 1
                if current_idx >= len(nums)-1:
                    break
        return jump_count
        """
        [2,3,1,1,4]
         ^   ^
         i   max
        """

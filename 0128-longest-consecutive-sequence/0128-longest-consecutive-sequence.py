class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                current_len = 1
                while current+1 in num_set:
                    current += 1
                    current_len += 1
                
                max_len = max(max_len, current_len)
        return max_len
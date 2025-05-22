class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count_dict = {}
        count = 1
        current = 0
        n = len(nums)
        while count <= n:
            if nums[current] not in num_count_dict:
                num_count_dict[nums[current]] = 1
                current += 1
            else:
                num_count_dict[nums[current]] += 1
                if num_count_dict[nums[current]] >= 3:
                    nums.pop(current)
                else:
                    current += 1
            count += 1

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        [-4, -1, -1, 0, 1, 2]
        """
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            while start < end:
                hap = nums[i] + nums[start] + nums[end]
                if hap < 0:
                    start += 1
                elif hap > 0:
                    end -= 1
                else:
                    result.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1

        return [list(num) for num in result]
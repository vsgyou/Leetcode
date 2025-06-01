class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        count = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                count = 1
            else:
                count += 1
            if count <= 2:
                nums[k] = nums[i]
                k += 1
        return k

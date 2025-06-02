class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        curr = float("inf") 
        count = 1
        for i in range(len(nums)):
            if nums[i] != curr:
                curr = nums[i]
                count = 1
            if count <= 2:
                nums[k] = nums[i]
                count+=1
                k += 1
        return k
                
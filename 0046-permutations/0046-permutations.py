class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(elements):
            if len(elements) == len(nums):
                result.append(elements[:])
                return
            for num in nums:
                if num in elements:
                    continue
                elements.append(num)
                backtrack(elements)
                elements.pop()
        backtrack([])
            
        return result
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
            
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        ex) [-2, 1, -3, 4,-1, 2, 1,-5, 4]
        dp= [-2, 1, -2, 4, 3, 5, 6, 1, 4]
          
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)
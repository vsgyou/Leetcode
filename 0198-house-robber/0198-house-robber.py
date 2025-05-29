class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        nums = [ 1, 2, 3, 4]        
        
        - 인덱스 0에 있는 집을 털었을 때 최대 금액 : nums[0] + F(nums[2:])
        - 인덱스 0에 있는 집을 안 털었을 때 최대 금액 : F[nums[1:]]

        F[nums] = MAX(nums[0] + F(nums[2:]), F[nums[1:]])
        F[start] = MAX(nums[start]) + F(start + 2), F(start + 1))
        """
        # def dfs(start):
        #     if start >= len(nums):
        #         return 0
        #     return max(nums[start] + dfs(start+2), dfs(start + 1))
        
        # return dfs(0)

        # 시간 복잡도 개선

        # memo = {}
        # def dfs(start):
        #     if start in memo:
        #         return memo[start]
        #     if start >= len(nums):
        #         return 0
        #     else:
        #         memo[start] = max(nums[start] + dfs(start + 2), dfs(start + 1))
        #     return memo[start]
        
        # return dfs(0)
        
        # DP해결법
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
        return dp[-1]
            



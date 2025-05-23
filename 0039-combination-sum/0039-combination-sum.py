class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        example) candidates = [2,3,5], target = 8
        []
        [2]
            [2,2]
                [2,2,2]
                    [2,2,2,2] = 8 ✅
                    [2,2,2,3] = 9 ❌
                    [2,2,2,5] = 11 ❌
                [2,2,3]
                    [2,2,3,2] = 9 ❌
                    [2,2,3,3] = 10 ❌
                    [2,2,3,5] = 12 ❌
                [2,2,5] = 9 ❌
            [2,3]
                [2,3,2]
                    [2,3,2,2] = 9 ❌
                    [2,3,2,3] = 10 ❌
                    [2,3,2,5] = 12 ❌
                [2,3,3] = 8 ✅
                [2,3,5] = 10 ❌
            [2,5]
                [2,5,2] = 9 ❌
                [2,5,3] = 10 ❌
                [2,5,5] = 12 ❌
        [3]
            [3,2] (위와 중복) ❌
            [3,3]
                [3,3,2] (위와 중복) ❌
                [3,3,3] = 9 ❌
                [3,3,5] = 11 ❌
            [3,5] = 8 ✅
            [3,5,3] (위와 중복) ❌
            [3,5,5] = 13 ❌ 
        [5]
            [5,2] (위와 중복) ❌
            [5,3] (위와 중복) ❌
            [5,5] = 10 ❌

        
        """
        
        result, nums = [], []
        def dfs(start, total):
            if total > target:
                return
            if total == target:
                result.append(nums[:])
            for i in range(start, len(candidates)):
                num = candidates[i]
                nums.append(num)
                dfs(i, num + total)
                nums.pop()
        dfs(0,0)    
        return result
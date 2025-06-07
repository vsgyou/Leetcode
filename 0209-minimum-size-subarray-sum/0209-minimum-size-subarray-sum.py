class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        nums = [2,3,1,2,4,3], target = 7
        [2] = 2
        [2,3] = 5
        [2,3,1] = 6
        [2,3,1,2] = 8
        [2,3,1,2,4] = 필요 x
        [2,3,1,2,4,3] = 필요 x
        ------------- min_len = 4
        [3] = 3
        [3,1] = 4
        [3,1,2] = 6
        [3,1,2,4] = 10
        [3,1,2,4,3] = 필요 x
        ------------ min_len =4
        [1] = 1
        [1,2] = 3
        [1,2,4] = 7
        [1,2,4,3] = 필요 x
        ------------ min_len = 3
        """
        # min_len = float("inf")
        # for i in range(len(nums)):
        #     tmp = []
        #     for j in range(i, min(i+min_len,len(nums))):
        #         tmp.append(nums[j])
        #         print(tmp, sum(tmp))
        #         if sum(tmp) >= target:
        #             min_len = min(len(tmp), min_len)
        #             break
        # if min_len == float("inf"):
        #     min_len = 0
        # return min_len            

        # 시간이 오래걸림 -> Sliding Window

        start = 0
        min_len = float("inf")
        curr_sum = 0
        for end in range(len(nums)):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_len = min(min_len, end - start +1)
                curr_sum -= nums[start]
                start += 1
        return min_len if min_len != float("inf") else 0

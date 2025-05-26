class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kadane(arr):
            max_sum = cur_sum = arr[0]
            for num in arr[1:]:
                cur_sum = max(num, cur_sum+num)
                max_sum = max(max_sum, cur_sum)
            return max_sum

        total_sum = sum(nums)
        max_kadane = kadane(nums)
        # 원형인 경우, 합이 가장 작은 배열을 빼면 원형의 경우 가장 큰 배열의 합이 나옴
        min_kadane = kadane([-num for num in nums])
        max_circular = total_sum + min_kadane

        return max(max_kadane, max_circular) if max_circular != 0 else max_kadane
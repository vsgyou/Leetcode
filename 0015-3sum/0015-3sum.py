class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                hap = nums[i] + nums[left] + nums[right]
                if hap < 0:
                    left += 1
                elif hap > 0:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return [list(num) for num in result]

        # 이전코드 
        # nums.sort()
        # result = []
        # for start in range(len(nums)-2):
        #     if start >0 and nums[start] == nums[start-1]:
        #         continue
        #     left = start + 1
        #     right = len(nums)-1
        #     while left < right:
        #         current_sum = nums[start] + nums[left] + nums[right]
        #         if current_sum == 0 :
        #             result.append([nums[start],nums[left],nums[right]])
        #             while left < right and nums[left] == nums[left + 1]:
        #                 left +=1 
        #             while left < right and nums[right] == nums[right -1]:
        #                 right -=1
        #             left +=1 
        #             right -= 1
        #         elif current_sum < 0:
        #             left += 1
        #         else:
        #             right -= 1
        # return result

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        max_amount = 0
        while left <= right:
            x = right - left
            y = min(height[right], height[left])
            max_amount = max(max_amount, x*y)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_amount
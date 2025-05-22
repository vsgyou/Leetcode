class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            length = min(height[left], height[right])
            area = width * length
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
            max_area = max(max_area,area)
        return max_area
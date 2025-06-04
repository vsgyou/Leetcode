class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_v = 0
        left, right = 0, len(height)-1
        while left < right:
            x = right - left
            y = min(height[right], height[left])
            max_v = max(max_v, x*y)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_v

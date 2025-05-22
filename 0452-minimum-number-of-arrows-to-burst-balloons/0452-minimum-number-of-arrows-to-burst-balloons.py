class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key = lambda x:x[1])
        num_dart = 1
        current_point = points[0][1] 
        for point in points:
            if current_point < point[0]:
                num_dart += 1
                current_point = point[1]
        return num_dart

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        
        return matrix

        """
        [1, 2, 3] [1, 4, 7] [7, 4, 1]
        [4, 5, 6] [2, 5, 8] [8, 5, 2]
        [7, 8, 9] [3, 6, 9] [9, 6, 3]
        """
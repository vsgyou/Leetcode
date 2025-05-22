class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_index.append([i,j])

        print(zero_index)

        for row,col in zero_index:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for i in range(len(matrix)):
                matrix[i][col] = 0
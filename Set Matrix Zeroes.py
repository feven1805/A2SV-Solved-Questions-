class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zeroRow = set()
        zeroCol = set()

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    zeroRow.add(row)
                    zeroCol.add(col)
        
        for row in range(rows):
            for col in range(cols):
                if row in zeroRow:
                    matrix[row][col] = 0
                if col in zeroCol:
                    matrix[row][col] = 0
            

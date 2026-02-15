class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        result = []

        for d in range(m + n - 1):
            diagonal = []
            
            if d < n:
                r, c = 0, d
            else:
                r, c = d - n + 1, n - 1
            
            while r < m and c >= 0:
                diagonal.append(mat[r][c])
                r += 1
                c -= 1
            
            if d % 2 == 0:
                result.extend(diagonal[::-1])
            else:
                result.extend(diagonal)

        return result
                    


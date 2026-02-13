class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
      
        row = len(img)
        col = len(img[0])
        res = [[0] * col for _ in range(row)]
    
        for r in range(row):
            for c in range(col):
                total = 0
                count = 0
                for i in range(r-1,r+2):
                    for j in range(c-1, c+2):
                        if (0 <= i < row) and (0 <= j < col):
                            total += img[i][j]
                            count += 1
                res[r][c] = total//count

        return res
                
        

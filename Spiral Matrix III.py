class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        result = []
        total = rows * cols
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        r, c = rStart, cStart
        result.append([r, c])
        
        steps = 1 
        
        while len(result) < total:
            for i in range(4):
                dr, dc = directions[i]
                
                if i == 2:
                    steps += 1
                
                for _ in range(steps):
                    r += dr
                    c += dc
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                
            steps += 1
        
        return result

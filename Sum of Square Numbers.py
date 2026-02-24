class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
     
        left = 0
        right = ceil(sqrt(c))
    
        while left <= right:
            l = left*left
            r = right*right
            if l + r == c:
                return True
            if l + r > c:
                right -= 1
            else:
                left += 1
        return False
        

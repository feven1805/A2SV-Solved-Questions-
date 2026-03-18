class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x , -n)
        y = self.myPow(x, n//2)
        if n%2 == 0:
            return y*y
        else:
            return y*y*x

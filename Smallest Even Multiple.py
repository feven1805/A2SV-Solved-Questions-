class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n%2 == 1:
            output = n*2
        else:
            output = n
        return output

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        reverse = x[::-1]
        if( x == reverse):
            return True
        else:
            return False

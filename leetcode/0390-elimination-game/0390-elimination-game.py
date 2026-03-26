class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = step = 1
        left = True
        remain = n
        while remain > 1:
            if left or remain % 2 == 1:
                head += step
            remain //= 2
            step *= 2
            left = not left
        return head


            
        
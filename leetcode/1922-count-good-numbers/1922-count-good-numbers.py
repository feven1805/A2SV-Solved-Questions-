class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        even = (n + 1) // 2  
        odd = n // 2          
        even_count = pow(5, even, MOD)
        odd_count = pow(4, odd, MOD)

        total = (even_count * odd_count) % MOD
        return total
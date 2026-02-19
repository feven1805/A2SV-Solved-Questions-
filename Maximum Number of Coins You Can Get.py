class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        print(piles)
        ans = 0
        count = len(piles)//3
        i = len(piles)-2
        while i >= 0 and count> 0:
            ans += piles[i]
            print(ans)
            count -= 1
            i -= 2
        return ans
                

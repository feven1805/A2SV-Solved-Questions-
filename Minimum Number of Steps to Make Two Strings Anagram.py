from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        countS = Counter(s)
        ans = 0
        
        for ch in t:
            if ch in countS and countS[ch] > 0:
                countS[ch] -= 1
                ans += 0
            elif ch not in countS or countS[ch] <= 0:
                ans += 1
        return ans

from collections import Counter
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        ans = ""
        count = Counter(s)
    
        for ch in order:
            if ch in count:
                ans += ch * count[ch]  
                count[ch] = 0 
       
        for ch in s:
            if count[ch] > 0:
                ans += ch * count[ch]
                count[ch] = 0
        
        return ans


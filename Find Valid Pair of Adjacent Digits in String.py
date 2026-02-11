from collections import Counter
class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        
        for i in range(len(s)-1):
            if (s[i] != s[i+1]) and (int(s[i]) == count[s[i]] and int(s[i+1]) == count[s[i+1]]):
                return s[i] + s[i+1]
        return ""

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        ans = ''
        sortedCount = sorted(count.items(), key=lambda item: item[1], reverse=True)
        
        for key, val in sortedCount:
            ans += key*val
        return ans
        

from collections import Counter
from collections import defaultdict

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mydict = defaultdict(list)
        ans = 0

        for index, num in enumerate(nums):
            mydict[num].append(index)
            
        for vals in mydict.values():
            if len(vals) < 2:
                continue
                
            for i in range(len(vals)):
                for j in range(i + 1, len(vals)):
                    idx1 = vals[i]
                    idx2 = vals[j]
                    if (idx1 * idx2) % k == 0:
                        ans += 1

        return ans



             

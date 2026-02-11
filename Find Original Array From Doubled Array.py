from collections import Counter
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed) % 2 != 0:
            return []

        ans = []
        changed.sort()
        count = Counter(changed)

        for n in changed:
            
            if count[n] == 0:
                continue
            if count[n*2] == 0:
                return []
                break

            ans.append(n)
            count[n] -= 1
            count[n*2] -= 1
            

        return ans

                

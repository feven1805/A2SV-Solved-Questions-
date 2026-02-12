class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        xy = 0
        yx = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1
        
        if (xy + yx) % 2 != 0:
            return -1
        
        swaps = 0
        
        swaps += xy // 2
        swaps += yx // 2
        
        if xy % 2 == 1:
            swaps += 2
        
        return swaps

class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort()
        for num in range(left, right+1):
            l = 0
            found = False
            while l < len(ranges):
                if ranges[l][0] <= num <= ranges[l][1]:
                    found = True
                    break
                else:
                    l += 1
            if found == False:
                return False  
        return True

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        dictr = {}
        returned = []
        for n in nums:
            if dictr.get(n,0) == 0:
                dictr[n] = dictr.get(n, 0) + 1
            else:
                returned.append(n)
        return returned

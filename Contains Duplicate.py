from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        """
        count = Counter(nums)
        for val in count.values():
            if val > 1:
                return True
            return False
        
        
        

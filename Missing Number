class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in nums:
            sum+= i
        realSum = 0
        for n in range(len(nums)+1):
            realSum += n
        missing = realSum - sum
        return missing

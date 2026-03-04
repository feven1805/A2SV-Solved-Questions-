class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 1
        result = [1] * (len(nums))
        prefix = [1]* (len(nums))
        for i in range(len(nums)):
            prefix[i] = left
            left *= nums[i]
            
        print(prefix)

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] = prefix[i] * suffix
            suffix *= nums[i]
        return result
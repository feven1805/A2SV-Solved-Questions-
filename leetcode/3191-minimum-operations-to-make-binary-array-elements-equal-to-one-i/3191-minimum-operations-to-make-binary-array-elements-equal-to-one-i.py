class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # """
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
            #    nums[i] ^= 1
               nums[i+1] ^= 1
               nums[i+2] ^= 1
               count += 1
                   
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        else:
            return count
       

                

      
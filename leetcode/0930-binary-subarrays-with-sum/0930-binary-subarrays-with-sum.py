class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = 0 
        summ = 0
        prefix = {0:1}

        for num in nums:
            summ += num
            if summ-goal in prefix:
                count += prefix[summ-goal]
            prefix[summ] = prefix.get(summ, 0) + 1
        return count
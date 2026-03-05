class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        prefix = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            prefix[i] = prefix[i-1] +  nums[i-1]
        print(prefix)

        for i in prefix:
            ans = min(ans, i)
        return 1-ans
            



        
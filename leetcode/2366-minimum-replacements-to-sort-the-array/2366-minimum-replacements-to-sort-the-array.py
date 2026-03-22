class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        mx = nums[-1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= mx:
                mx = nums[i]
            else:
                k = (nums[i] + mx - 1) // mx
                ans += k - 1
                mx = nums[i] // k
        
        return ans
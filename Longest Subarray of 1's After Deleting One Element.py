class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return len(nums) - 1

        n = len(nums)
        ans = 0
        
        for i in range(n):
            if nums[i] == 0:
                left = 0
                j = i - 1
                while j >= 0 and nums[j] == 1:
                    left += 1
                    j -= 1

                right = 0
                j = i + 1
                while j < n and nums[j] == 1:
                    right += 1
                    j += 1
                
                ans = max(ans, left + right)
        
        return ans

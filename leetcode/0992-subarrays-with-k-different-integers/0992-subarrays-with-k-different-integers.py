from collections import defaultdict
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        left1 = left2 = ans = 0
        
        for right in range(len(nums)):
            count1[nums[right]] += 1
            count2[nums[right]] += 1
            
            while len(count1) > k:
                count1[nums[left1]] -= 1
                if count1[nums[left1]] == 0:
                    del count1[nums[left1]]
                left1 += 1
            
            while len(count2) > k - 1:
                count2[nums[left2]] -= 1
                if count2[nums[left2]] == 0:
                    del count2[nums[left2]]
                left2 += 1
            
            ans += left2 - left1
        
        return ans

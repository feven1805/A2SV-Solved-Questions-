class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0

        nums2 = set(nums)   
        nums3 = list(nums2)
        nums3.sort()

        ans = 1
        count = 1

        for i in range(1, len(nums3)):
            if nums3[i] == nums3[i-1] + 1:
                count += 1
            else:
                count = 1

            ans = max(ans, count)

        return ans

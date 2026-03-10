class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        diff = [0]*(n+1)

        for l, r in requests:
            diff[l] += 1
            if r+1 < n:
                diff[r+1] -= 1

        freq = [0]*n
        curr = 0
        for i in range(n):
            curr += diff[i]
            freq[i] = curr

        nums.sort()
        freq.sort()

        MOD = 10**9 + 7
        ans = 0

        for i in range(n):
            ans = (ans + nums[i]*freq[i]) % MOD

        return ans
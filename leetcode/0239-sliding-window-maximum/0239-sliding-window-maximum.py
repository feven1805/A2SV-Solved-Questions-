class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        ans = []
        left  = window = 0
        for right in range(len(nums)):
            while  dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if dq[0] <= right - k:
                dq.popleft()

            if right >= k - 1:
                ans.append(nums[dq[0]])

        return ans
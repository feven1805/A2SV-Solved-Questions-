class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        minP = deque()
        maxP = deque()
        stack = []
        res = left =  0

        for i in range(len(nums)):
            while minP and minP[-1] > nums[i]: 
                minP.pop()
            minP.append(nums[i])

            while maxP and maxP[-1] < nums[i]:
                maxP.pop()
            maxP.append(nums[i])
            # print(minP)
            # print(maxP)
            while maxP[0] - minP[0] > limit:
                if nums[left] == minP[0]:
                    minP.popleft()
                if nums[left] == maxP[0]:
                    maxP.popleft()
                left += 1
            res = max(res, i-left+1)
        return res

  


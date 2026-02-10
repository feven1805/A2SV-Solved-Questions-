class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        even_sum = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_sum += nums[i]

        for i in range(len(queries)):
            val = queries[i][0]
            idx = queries[i][1]
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            nums[idx] = nums[idx] + val

            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            ans.append(even_sum)

        return ans



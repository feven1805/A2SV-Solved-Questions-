class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        n = len(nums)

        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        result = "".join(nums)
        if result[0] == "0":
            return "0"
        return result


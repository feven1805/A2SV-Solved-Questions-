class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)/3
        ans = []
        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict:
                mydict[nums[i]] += 1
            else:
                mydict[nums[i]] = 1
        for key,value in mydict.items():
            if value > n:
                ans.append(key)
        return ans

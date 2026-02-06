class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myDict = {}
        res = 0

        for num in nums:
            if num in myDict:
                myDict[num] += 1
            else:
                myDict[num] = 1
   
        for num, count in myDict.items():
            if count == 1:
                res = num
                break 
        return res

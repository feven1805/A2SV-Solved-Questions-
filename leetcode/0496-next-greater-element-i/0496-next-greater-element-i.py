class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        greater = {}
        res = []

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        print(stack)

        for num in stack:
            greater[num] = -1
        
        for num in nums1:
            res.append(greater[num])
        return res
        


        


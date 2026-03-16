class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        x = float('-inf')

        for num in reversed(nums):
            if num < x:
                return True
            while stack and num > stack[-1]:
                x = stack.pop()
            stack.append(num)
        
        return False
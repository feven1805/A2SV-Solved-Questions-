class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        maxArea = 0
       
        while left < right:
            w = abs(left - right)
            h = min(height[left], height[right])
            maxArea = max(maxArea, h*w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


        
        

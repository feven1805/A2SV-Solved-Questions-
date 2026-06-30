class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        countEven = 0
        countOdd = 1
        for i in nums:
            if i % 2 == 0:
                ans[countEven] = i
                countEven += 2
            else:
                ans[countOdd] = i
                countOdd += 2
        return ans
            

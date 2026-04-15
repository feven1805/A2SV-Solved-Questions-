class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      
        arr = []
        for i in range(len(nums) + 1):
            arr.append(i)
        sum1 = sum(nums)
        sum2 = sum(arr) 
        print(sum1, sum2)
       
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] > 1:
                ans = num
        return([ans,ans + (sum2 - sum1) ])



      

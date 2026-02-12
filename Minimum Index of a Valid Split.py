from collections import Counter

class Solution(object):
    def minimumIndex(self, nums):
        n = len(nums)
        count = Counter(nums)
        dominant = max(count, key=count.get)
        total = count[dominant]
        
        leftDom = 0
        
        for i in range(n - 1):
            if nums[i] == dominant:
                leftDom += 1
            
            leftLen = i + 1
            rightLen = n - i - 1
            rightDom = total - leftDom
            
            if leftDom > leftLen // 2 and rightDom > rightLen // 2:
                return i
        
        return -1

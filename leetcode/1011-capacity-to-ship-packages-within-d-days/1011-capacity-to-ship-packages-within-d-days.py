class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            d, curr = 1, 0
            for w in weights:
                if curr + w > mid:
                    d += 1
                    curr = 0
                curr += w
            
            if d <= days:
                right = mid
            else:
                left = mid + 1
        
        return left
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
  
        heaters.sort()
        def findmin(h):
            low, high = 0, len(heaters) - 1
            ans = float('inf')

            while low <= high:
                mid = (low + high) // 2
                ans = min(ans, abs(heaters[mid] - h))

                if heaters[mid] < h:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans

        maxD = 0
        for h in houses:
            minD = findmin(h)
            maxD = max(maxD, minD)

        return maxD
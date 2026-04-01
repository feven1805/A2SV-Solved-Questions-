class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        ans = 0

        while left <= right:
            mid = (left + right)//2
            length = len(citations) - mid
            if citations[mid] == length:
                return length
            elif citations[mid] < length:
                left = mid + 1
            else:
                right = mid - 1
        return len(citations) - left
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
      
        n = len(nums)
        result = [0] * n

        arr = list(enumerate(nums))
        
        def merge_sort(left, right):
            if right - left <= 1:
                return arr[left:right]
            
            mid = (left + right) // 2
            L = merge_sort(left, mid)
            R = merge_sort(mid, right)
            
            merged = []
            i = j = 0
            right_count = 0
            
            while i < len(L) and j < len(R):
                if L[i][1] <= R[j][1]:
                    result[L[i][0]] += right_count
                    merged.append(L[i])
                    i += 1
                else:
                    right_count += 1
                    merged.append(R[j])
                    j += 1
            
            while i < len(L):
                result[L[i][0]] += right_count
                merged.append(L[i])
                i += 1
            
            while j < len(R):
                merged.append(R[j])
                j += 1
            
            return merged
        
        arr[:] = merge_sort(0, n)
        return result
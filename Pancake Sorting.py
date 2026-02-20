class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        result = []
        for size in range(n, 1, -1):
            max_index = arr.index(size)
            if max_index == size - 1:
                continue

            if max_index != 0:
                result.append(max_index + 1)
                arr[0:max_index + 1] = reversed(arr[0:max_index + 1])

            result.append(size)
            arr[:size] = reversed(arr[:size])
        
        return result

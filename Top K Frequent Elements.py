from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        freq2 = []
        freq = Counter(nums)
        for key in freq:
            freq2.append([key, freq[key]])
        freq2.sort(key =lambda item: item[1], reverse = True)
        for i in range(k):
                ans.append(freq2[i][0])
        return ans

        

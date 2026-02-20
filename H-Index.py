class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = 0
        citations.sort(reverse = True)
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                count += 1
            else:
                break
        return count

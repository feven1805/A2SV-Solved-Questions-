from collections import Counter
class Solution(object):
    def findCommonResponse(self, responses):
        """
        :type responses: List[List[str]]
        :rtype: str
        """
        setResp = []
        for sublist in responses:
            setResp.append(set(sublist))


        count = Counter()
        for day in setResp:
            count.update(day)


        max_freq = max(count.values())

        candidates = []
        for resp, freq in count.items():
            if freq == max_freq:
                candidates.append(resp)

        result = min(candidates)

        return result

    

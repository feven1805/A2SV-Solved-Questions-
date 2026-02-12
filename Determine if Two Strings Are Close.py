from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        list1 = []
        list2 = []
        count1 = Counter(word1)
        count2 = Counter(word2)
        if len(word1) != len(word2):
            return False
        for ch1 in word1:
            if ch1 not in word2:
                return False
        for ch2 in word2:
            if ch2 not in word1:
                return False

        sortedCount1 = list(sorted(count1.items() , key=lambda item: item[1]))
        sortedCount2 = list(sorted(count2.items(), key= lambda item: item[1]))
        sortedCount1 = [list(item) for item in sortedCount1]
        sortedCount2 = [list(item) for item in sortedCount2]

        for i in range(len(sortedCount1)):
            list1.append(sortedCount1[i][1])
        for i in range(len(sortedCount2)):
            list2.append(sortedCount2[i][1])

        if list1 == list2:
             return True
        return False

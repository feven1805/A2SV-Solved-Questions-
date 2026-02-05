class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        x = float('inf')
        newlist = []
        for str1 in list2:
            if str1 in list1:
                i = list1.index(str1)
                j = list2.index(str1)
                x = min(i+j, x)

        for str1 in list2:
            if str1 in list1:
                i = list1.index(str1)
                j = list2.index(str1)
                if x == i+j:
                    newlist.append(str1)
        return newlist
        

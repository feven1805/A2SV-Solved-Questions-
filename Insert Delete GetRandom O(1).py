import random
from collections import defaultdict
class RandomizedSet(object):
    
    def __init__(self):
        self.mydict = defaultdict(int)

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.mydict:
            self.mydict[val] += 1
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mydict:
            del self.mydict[val]
            return True
        return False


    def getRandom(self):
        """
        :rtype: int
        """
        rand = random.choice(self.mydict.keys())
        return rand
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

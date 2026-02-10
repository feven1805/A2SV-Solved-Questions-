from collections import defaultdict
class FrequencyTracker(object):
    def __init__(self):
        self.occ = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number):
        self.occ[number] += 1
        f = self.occ[number]
        self.freq[f] += 1
        if (f-1) > 0:
            self.freq[f-1] -= 1
        

    def deleteOne(self, number):
        if self.occ[number] > 0:
            self.occ[number] -= 1
            f = self.occ[number]
            self.freq[f] += 1
            self.freq[f+1] -= 1
      

    def hasFrequency(self, frequency):
        if self.freq[frequency] > 0:
            return True
        return False 
        

    

    



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

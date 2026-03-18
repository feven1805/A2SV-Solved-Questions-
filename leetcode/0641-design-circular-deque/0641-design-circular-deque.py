class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = deque()
        self.k = k
        self.size = 0
    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False
        self.q.appendleft(value)
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.size == self.k:
            return False
        self.q.append(value)
        self.size += 1
        return True 
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if not self.q:
            return False
        else:
            self.size -= 1 
            self.q.popleft()
            return True
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.size == 0:
            return False
        else:
            self.q.pop()
            self.size -= 1
            return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1
        return self.q[0]


    def getRear(self):
        """
        :rtype: int
        """
        if not self.q:
            return -1
        return self.q[-1]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if not self.q:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        if self.size == self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
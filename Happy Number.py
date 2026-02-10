class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mySet=set()
        while n!=1 :
            if n in mySet:
                return False
            mySet.add(n)
            total=0
            while n>0:
                r=n%10
                total+=r*r
                n=n//10
            n = total
        return True
        

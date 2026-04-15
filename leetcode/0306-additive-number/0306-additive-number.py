class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i + 1, n):
                num1 = num[:i]
                num2 = num[i:j]
          
                if (num1[0] == '0' and len(num1) > 1) or  (num2[0] == '0' and len(num2) > 1):
                    continue
                
                if self.check(num1, num2, num[j:]):
                    return True
        
        return False

    def check(self, a, b, remaining):
        while remaining:
            s = str(int(a) + int(b))
            
            if not remaining.startswith(s):
                return False
            
            remaining = remaining[len(s):]
            a, b = b, s
        
        return True
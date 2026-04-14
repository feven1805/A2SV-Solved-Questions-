class Solution:
    def splitString(self, s: str) -> bool:
        def func(ind,prev):
            if ind == len(s):
                return True
            ans = 0
            for i in range(ind,len(s)):
                ans = (ans * 10) + int(s[i]) 
                if ans == prev - 1:
                    if func(i+1,ans):
                        return True
                if ans >= prev:
                    break
            return False
        for j in range(1, len(s)):
            check = int(s[:j])
            if func(j, check):
                return True
        return False
                

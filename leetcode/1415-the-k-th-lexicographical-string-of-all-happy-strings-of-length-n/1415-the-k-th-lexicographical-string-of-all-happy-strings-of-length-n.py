class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        curr = ''
        ans = []
        self.happyStrings(n, curr, ans)

        if len(ans) < k:
            return ''
        return ans[k-1]
    
    def happyStrings(self, n, curr, ans):
        if len(curr) == n:
            ans.append(curr)
            return

        for c in ['a', 'b', 'c']:
            if len(curr) > 0 and curr[-1] == c:
                continue

            self.happyStrings(n, curr + c, ans)
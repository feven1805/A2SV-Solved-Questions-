class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        curr = []
        wordSet = set(wordDict)
        self.func(ans, wordSet, s, curr, 0)
        return ans
        
    def func(self,ans, wordSet, s, curr, start):

        if start == len(s):
            ans.append(" ".join(curr)) 
            return ans
        for end in range(start + 1, len(s) + 1):
            word = s[start : end]
            if word in wordSet:
                curr.append(word)
                self.func(ans, wordSet, s, curr, end)
                curr.pop()
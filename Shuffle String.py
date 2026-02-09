class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ans = [""]*len(s)
        for ch, z in zip(s, indices):
            ans[z] = ch
        
        return "".join(ans)

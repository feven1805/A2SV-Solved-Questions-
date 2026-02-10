class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s2 = ''.join(sorted(s))
        t2 = ''.join(sorted(t))
        if s2 == t2:
            return True
        return False

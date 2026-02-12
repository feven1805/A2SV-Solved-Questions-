from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomCount = Counter(ransomNote)
        magCount = Counter(magazine)

        for ch in ransomNote:
            if ch in magazine and (magCount[ch] >= ransomCount[ch]):
                continue
            else:
                return False
        return True

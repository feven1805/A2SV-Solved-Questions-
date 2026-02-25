class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        s = sum(skill)

        if s % (n//2) != 0:
            return(-1)

        skill.sort()
        left = 0
        chemistry = 0
        right = n-1
        team = []
        target = s // (n//2)
        while left < right:
            if skill[left] + skill[right] != target:
                return -1  
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1

        return chemistry
        
            

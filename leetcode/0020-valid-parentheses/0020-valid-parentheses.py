class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapp = { ')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in mapp:
                if not stack:
                    return False
                top = stack.pop()
                if top != mapp[c]:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False
                

    
        
        
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for log in logs:
            if log == '../' and stack:
                stack.pop()
            elif log == '../' and not stack:
                continue
            elif log == './':
                continue
            else:
                stack.append(log)
        return(len(stack))
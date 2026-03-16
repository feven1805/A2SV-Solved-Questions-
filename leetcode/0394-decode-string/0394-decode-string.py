class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                
                substr = ''.join(temp[::-1])
                stack.pop() 
                
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(substr * int(num))
        
        return ''.join(stack)


                


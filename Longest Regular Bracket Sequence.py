s = input()
stack = [-1]
max_len = 0
count = 0
 
for i, c in enumerate(s):
    if c == '(':
        stack.append(i)
    else:
        stack.pop()
        if stack:
            length = i - stack[-1]
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1
        else:
            stack.append(i)
 
if max_len == 0:
    count = 1
 
print(max_len, count)

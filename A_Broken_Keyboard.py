numtest = int(input())
for _ in range(numtest):
    s = input() 
    i = 0
    res = set()
    
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 2
        else:
            res.add(s[i])
            i += 1
    print(''.join(sorted(res)))

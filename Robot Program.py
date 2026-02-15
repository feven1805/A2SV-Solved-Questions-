t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pref = 0
    first = -1

    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        
        if x + pref == 0:
            first = i + 1
            break
    
    if first == -1 or first > k:
        print(0)
        continue
    
    pref = 0
    cycle = -1
    
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        
        if pref == 0:
            cycle = i + 1
            break
    
    if cycle == -1:
        print(1)
    else:
        print(1 + (k - first) // cycle)

    
    



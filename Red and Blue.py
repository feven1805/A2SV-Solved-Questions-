t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    max_r = current_r = 0
    for x in r:
        current_r += x
        max_r = max(max_r, current_r)
    
    max_b = current_b = 0
    for x in b:
        current_b += x
        max_b = max(max_b, current_b)
    
    print(max_r + max_b)

numtest = int(input())
for _ in range(numtest):
    n = int(input())
    p = list(map(int, input().split()))
    ans = []
    ans.append(p[0]) 
    
    for i in range(1, n-1):
        if (p[i] - p[i-1]) * (p[i+1] - p[i]) < 0:
            ans.append(p[i])
    ans.append(p[-1])
    
    print(len(ans))
    print(*ans)

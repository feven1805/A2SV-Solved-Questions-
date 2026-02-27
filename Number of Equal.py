from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i,j, ans = 0,0,0
while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        countA = 0
        val = a[i]
        while i + countA < n and a[i + countA] == val:
            countA += 1
        
        countB = 0
        while j + countB < m and b[j + countB] == val:
            countB += 1

        ans += countB * countA
        i += countA
        j = countB
print(ans)
                
                

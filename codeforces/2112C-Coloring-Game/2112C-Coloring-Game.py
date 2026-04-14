def upper_bound(arr, left, right, target):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    
    for i in range(n):
        for j in range(i):
            x = max(a[n - 1], 2 * a[i]) - a[i] - a[j]
            
            k = upper_bound(a, 0, j, x)
            ans += j - k
    
    print(ans)
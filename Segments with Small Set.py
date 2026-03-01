from collections import defaultdict

n,k = map(int, input().split())
arr = list(map(int, input().split()))
left = ans = unique = 0
count = defaultdict(int)
for right in range(n):
    if count[arr[right]] == 0:
        unique += 1
    count[arr[right]] += 1
    while unique > k:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            unique -= 1
        left += 1
    ans += right - left + 1
print(ans)
        




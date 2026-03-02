from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = defaultdict(int)
distinct = best_len =best_r = best_l = left = 0

for right in range(n):
    x = arr[right]
    if count[x] == 0:
        distinct += 1
    count[x] += 1

    while distinct > k:
        y = arr[left]
        count[y] -= 1
        if count[y] == 0:
            distinct -= 1
        left += 1

    length = right - left + 1
    if length > best_len:
        best_len = length
        best_l = left
        best_r = right
        
print(best_l + 1, best_r + 1)

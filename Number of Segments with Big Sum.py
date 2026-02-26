n, m = map(int, input().split())
s = list(map(int, input().split()))
sum = 0
left = 0
count = 0
for right in range(n):
    sum += s[right]
    while sum >= m:
        sum -= s[left]
        left += 1
        count += n-right
print(count)

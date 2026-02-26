n , m = map(int, input().split())
s = list(map(int, input().split()))

left, sum, count = 0,0,0
for right in range(n):
    sum += s[right]
    while sum > m:
        sum -= s[left]
        left += 1
    count += (right - left + 1)   
print(count)
        

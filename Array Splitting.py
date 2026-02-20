n , k = map(int, input().split())
arr = input().split()

diff = []
for i in range(len(arr)-1):
    x = int(arr[i+1]) - int(arr[i])
    diff.append(x)
diff.sort()
ne = k-1
needed = n - ne
sum = 0
for i in range(needed-1):
    sum += diff[i]
print(sum)


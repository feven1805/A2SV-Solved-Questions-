n = int(input())
a = list(map(int, input().split()))
a.sort()
day = 1
for i in a:
    if i >= day:
        day += 1
    else:
        continue
print(day-1)

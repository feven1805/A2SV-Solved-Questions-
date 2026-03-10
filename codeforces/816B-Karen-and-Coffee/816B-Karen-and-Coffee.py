maxx = 1000000
n, k, q = map(int, input().split())
diff = [0]*(maxx+2)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r+1] -= 1

cover = [0]*(maxx+2)
for i in range(1, maxx+1):
    cover[i] = cover[i-1] + diff[i]

valid = [0]*(maxx+2)
for i in range(1, maxx+1):
    if cover[i] >= k:
        valid[i] = 1

pref = [0]*(maxx+2)
for i in range(1, maxx+1):
    pref[i] = pref[i-1] + valid[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(pref[b] - pref[a-1])
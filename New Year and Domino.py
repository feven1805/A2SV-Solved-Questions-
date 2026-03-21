h, w = map(int, input().split())
grid = []
for _ in range(h):
    s = input().strip()
    grid.append(s)

H = []
V = []
for i in range(h):
    rowH = []
    rowV = []
    for j in range(w):
        rowH.append(0)
        rowV.append(0)
    H.append(rowH)
    V.append(rowV)

for i in range(h):
    for j in range(w-1):
        if grid[i][j] == '.' and grid[i][j+1] == '.':
            H[i][j] = 1

for i in range(h-1):
    for j in range(w):
        if grid[i][j] == '.' and grid[i+1][j] == '.':
            V[i][j] = 1

prefH = []
prefV = []
for i in range(h+1):
    rowH = []
    rowV = []
    for j in range(w+1):
        rowH.append(0)
        rowV.append(0)
    prefH.append(rowH)
    prefV.append(rowV)

for i in range(1, h+1):
    for j in range(1, w+1):
        prefH[i][j] = prefH[i-1][j] + prefH[i][j-1] - prefH[i-1][j-1] + H[i-1][j-1]
        prefV[i][j] = prefV[i-1][j] + prefV[i][j-1] - prefV[i-1][j-1] + V[i-1][j-1]

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    ansH = 0
    if c1 <= c2-1:
        ansH = prefH[r2][c2-1] - prefH[r1-1][c2-1] - prefH[r2][c1-1] + prefH[r1-1][c1-1]
    ansV = 0
    if r1 <= r2-1:
        ansV = prefV[r2-1][c2] - prefV[r1-1][c2] - prefV[r2-1][c1-1] + prefV[r1-1][c1-1]
    print(ansH + ansV)

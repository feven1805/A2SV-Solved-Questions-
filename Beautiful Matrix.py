matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 1:
            r,c = row,col
ans = 0
num1 = abs(2-r)
num2 = abs(2-c)
ans = num1 + num2
print(ans)

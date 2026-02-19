n = int(input())
x = list(map(int, input().split()))

x.sort()  
middle_index = (n - 1) // 2
print(x[middle_index])

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    balance = [0] * n
    count = 0
    
    for i in range(n):
        if a[i] == '1':
            count += 1
        else:
            count -= 1
        balance[i] = count
    
    flip = 0  
    possible = True

    for i in range(n - 1, -1, -1):
        current_bit = int(a[i])
        if flip:
            current_bit ^= 1
        
        if current_bit != int(b[i]):

            if balance[i] == 0:
                flip ^= 1  
            else:
                possible = False
                break
    
    print("YES" if possible else "NO")


t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    answer = -1
    
    for i in range(n - 1):
        if s[i] == 'a' and s[i + 1] == 'a':
            answer = 2
            break
    
    if answer == -1:
        for i in range(n - 2):
            if s[i] == 'a' and s[i + 2] == 'a':
                answer = 3
                break
    

    if answer == -1:
        for i in range(n - 3):
            if s[i] == 'a' and s[i + 3] == 'a':
                if s[i+1] != 'a' and s[i+2] != 'a':
                    answer = 4
                    break
    
    print(answer)

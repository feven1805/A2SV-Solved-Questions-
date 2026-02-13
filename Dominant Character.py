
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    ans = -1
    found = False
    for length in (2,3,4,7):
        for i in range(n-length + 1):
            sub = s[i: i+length]
            a = sub.count('a')
            b = sub.count('b')
            c = sub.count('c')

            if a > b and a > c:
                ans = length
                found = True
                break
            else:
                found = False
        if found:
            break
    print(ans)








t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()
    prev = float('-inf')
    possible = True

    for J in range(n):
        if a[J] >= prev:
            choice1 = a[J]
        else:
            choice1 = float('inf')

        target = prev + a[J]
        low = 0
        high = m - 1
        idx = m

        while low <= high:
            mid = (low + high) // 2
            if b[mid] >= target:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1

        if idx < m:
            choice2 = b[idx] - a[J]
        else:
            choice2 = float('inf')

        ans = min(choice1, choice2)

        if ans == float('inf'):
            possible = False
            break

        prev = ans

    print('YES' if possible else 'NO')
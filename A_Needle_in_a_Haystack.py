from collections import Counter
numtest = int(input())
for _ in range(numtest):
    s = input()
    t = input()
    countS = Counter(s)
    countT = Counter(t)

    for ch in s:
        if countS[ch] > countT[ch]:
            print('Impossible')
            break
    else:
        leftover_counter = countT - countS
        list2 = sorted(leftover_counter.elements())  # renamed leftover → list2

        ans = []
        i,j = 0,0
        n = len(list2)
        while i < n and j < len(s):
            if list2[i] < s[j]:
                ans.append(list2[i])
                i += 1
            else:
                ans.append(s[j])
                j += 1

        while i < n:
            ans.append(list2[i])
            i += 1

        while j < len(s):
            ans.append(s[j])
            j += 1
        print(''.join(ans))




def backtrack(i, curr):
    global total, valid

    if i == len(s2):
        total += 1
        if curr == target:
            valid += 1
        return

    if s2[i] == '+':
        backtrack(i + 1, curr + 1)
    elif s2[i] == '-':
        backtrack(i + 1, curr - 1)
    else:
        backtrack(i + 1, curr + 1)
        backtrack(i + 1, curr - 1)

backtrack(0, 0)

print(valid / total)
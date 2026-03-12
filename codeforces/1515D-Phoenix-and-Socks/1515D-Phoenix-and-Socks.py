from collections import Counter
    left_count = Counter(left_colors)
    right_count = Counter(right_colors)

    for c in list(left_count.keys()):
        if c in right_count:
            match = min(left_count[c], right_count[c])
            left_count[c] -= match
            right_count[c] -= match
            l -= match
            r -= match
            if left_count[c] == 0:
                del left_count[c]
            if right_count[c] == 0:
                del right_count[c]

    if l > r:
        big_side = left_count
        small_side = right_count
        diff = l - r
    else:
        big_side = right_count
        small_side = left_count
        diff = r - l

    cost = 0
    to_convert = diff // 2
    pairs_possible = 0
    for c, cnt in list(big_side.items()):
        can_pair = cnt // 2
        use = min(can_pair, to_convert)
        cost += use
        big_side[c] -= use * 2
        to_convert -= use

    cost += to_convert  
    remains = sum(left_count.values()) + sum(right_count.values())
    cost += remains // 2
    print(cost)
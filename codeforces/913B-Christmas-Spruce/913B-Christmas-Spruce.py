from collections import defaultdict

n = int(input())
dict1 = defaultdict(list)
dict2 = defaultdict(int)
ans = True
for i in range(1,n):
    p = int(input())
    dict1[p].append(i + 1)

# print(dict1)
# print(dict2)
for key,arr in dict1.items():
    dict2[key] = 0 
    for a in arr:
        if a not in dict1:
            dict2[key] += 1
  
# print(dict2)
# print(dict2.values())
for val in dict2.values():
    if val >= 3: 
        ans = True
    else:
        ans = False
        break
if ans:
    print('Yes')
else:
    print('No')
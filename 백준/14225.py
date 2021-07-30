from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

res = set()

for i in range(1, n+1):
    for comb in combinations(arr, i):
        res.add(sum(comb))

for i in range(1, max(res)):
    if i not in res:
        print(i)
        break
else:
    print(max(res)+1)

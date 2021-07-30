from itertools import combinations

n, m = map(int, input().split())

arr = list(map(int, input().split()))

max_ = 0
for comb in combinations(arr, 3):
    s = sum(comb)
    if s <= m and s > max_:
        max_ = s
print(max_)
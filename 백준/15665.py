from itertools import product

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = set()
for comb in product(*[arr for _ in range(k)]):
    ans.add(comb)

ans = sorted(list(ans))
for a in ans:
    print(str(a)[1:-1].replace(',', ''))
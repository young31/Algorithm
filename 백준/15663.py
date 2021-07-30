from itertools import permutations

n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = set()
for comb in permutations(sorted(arr), k):
    ans.add(comb)

ans = sorted(list(ans))
for a in ans:
    print(str(a)[1:-1].replace(',', ''))
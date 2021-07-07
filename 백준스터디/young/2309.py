from itertools import combinations

h = [int(input()) for _ in range(9)]

for comb in combinations(h, 7):
    if sum(comb) == 100:
        ans = sorted(list(comb))
        print(ans)
        for a in ans: print(a)
        break
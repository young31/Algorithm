from itertools import permutations

n, k = map(int, input().split())

for comb in permutations(range(1, n+1), k):
    print(str(comb)[1:-1].replace(',', ''))
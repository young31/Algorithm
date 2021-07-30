from itertools import permutations

n, k = map(int, input().split())
arr = list(map(int, input().split()))

for comb in permutations(sorted(arr), k):
    print(str(comb)[1:-1].replace(',', ''))
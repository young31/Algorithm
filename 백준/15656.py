from itertools import product

n, k = map(int, input().split())
arr = list(map(int, input().split()))

for comb in product(*[sorted(arr) for _ in range(k)]):
    print(str(comb)[1:-1].replace(',', ''))
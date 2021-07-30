from itertools import product

n, k = map(int, input().split())

for comb in product(*[range(1, n+1) for _ in range(k)]):
    print(str(comb)[1:-1].replace(',', ''))
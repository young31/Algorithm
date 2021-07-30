from itertools import combinations

while 1:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break
    n = arr[0]
    arr = sorted(arr[1:])
    for comb in combinations(arr, 6):
        print(*comb)

    print()




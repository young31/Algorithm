import sys
sys.stdin = open("./swexpert_/input.txt", "r")

from itertools import permutations

T = int(input())
for test_case in range(1, T+1):
    n = int(input())

    arr = [list(map(int, input().split(' '))) for _ in range(n)]
    min_ = sum([arr[i][i] for i in range(n)])

    for perm in permutations(range(n)):
        ans = 0
        for i, p in enumerate(perm):
            ans += arr[i][p]
            if ans >= min_:
                break

        if ans < min_:
            min_ = ans
    
    print(f'#{test_case} {min_}')
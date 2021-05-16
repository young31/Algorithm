import sys
sys.stdin = open("./swexpert_/input.txt", "r")

from itertools import combinations

T = int(input())
for test_case in range(1, T+1):
    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))

    cnt = 0
    for i in range(1, n):
        for c in combinations(arr, i):
            if sum(c) == k:
                cnt += 1

    print(f'#{test_case} {cnt}')
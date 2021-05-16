import sys
sys.stdin = open("./swexpert_/input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    p = list(map(int, input().split(' ')))
    
    cnt = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] < p[i+1] or p[i+1] < p[i] < p[i-1]:
            cnt += 1

    print(f'#{test_case} {cnt}')
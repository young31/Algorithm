import sys
sys.stdin = open("./swexpert_/input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    d, l, n = map(int, input().split(' '))
    answer = d*n + d//100 * n*(n-1)//2 * l
    print(f'#{test_case} {answer}')
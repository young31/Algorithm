import sys
sys.stdin = open("./swexpert_/input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    s = list(input())

    if len(set(s)) == 2 and s.count(s[0]) == 2:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
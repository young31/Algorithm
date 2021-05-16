import sys
sys.stdin = open("./swexpert_/input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    directions = input()
    n = len(directions)
    a, b = 1, 1
    
    for i in range(n):
        if directions[i] == 'L':
            a, b = a, a+b
        else:
            a, b = a+b, b
    
    print(f'#{test_case} {a} {b}')
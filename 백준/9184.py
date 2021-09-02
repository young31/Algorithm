from collections import defaultdict
import sys
input = sys.stdin.readline

def w(a, b, c):
    if memo[(a,b,c)]:
        return memo[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:
        memo[(a,b,c)] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        memo[(a,b,c)] = w(20, 20, 20)
        return memo[(a,b,c)]

    elif a < b and b < c:
        memo[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[(a,b,c)]
    else:
        memo[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[(a,b,c)]

def false(): return False
memo = defaultdict(false)

while 1:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    else:
        if memo[(a,b,c)]:
            res = memo[(a,b,c)]
        else:
            res = w(a, b, c)
            memo[(a,b,c)] = res
        print(f'w({a}, {b}, {c}) = {res}')
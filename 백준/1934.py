import sys
input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def LCM(a, b):
    return a * b // GCD(a, b)

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))
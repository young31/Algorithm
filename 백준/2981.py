import math
import sys
input = sys.stdin.readline

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

N = int(input())
arr = [int(input()) for _ in range(N)]
arr_ = []
for i in range(N-1):
    arr_.append(abs(arr[i+1]-arr[i]))

while len(arr_) > 1:
    for k in range(len(arr_)-1):
        arr_[k] = GCD(arr_[k], arr_[k+1])
    arr_.pop()

n = arr_[0]
ans = set()
for i in range(1, math.ceil(math.sqrt(n))+1):
    if n % i == 0:
        ans.add(i)
        ans.add(n//i)

print(*sorted((ans -set([1]))))


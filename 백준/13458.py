import math

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

answer = sum([max(math.ceil((a-b)/c), 0) for a in arr])+n
print(answer)
n, m, k = map(int, input().split())

for _ in range(k):
    if n > 2*m:
        n -= 1
    else:
        m -= 1

print(min(n//2, m))
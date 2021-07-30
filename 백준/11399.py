n = int(input())

arr = sorted(list(map(int, input().split())))

ans = 0
for i, a in enumerate(arr):
    ans += (n-i)*a
print(ans)
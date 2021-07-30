n = int(input())

arr = [
    tuple(map(int, input().split())) for _ in range(n)
]

ans = []
for a in arr:
    sub = list(filter(lambda x: x[0] > a[0] and x[1] > a[1], arr))
    ans.append(len(sub)+1)

print(*ans)
n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))
    
def solution(n, table):
    ans = [0 for _ in range(n)]

    for i, (d, p) in enumerate(table):
        if i+d-1 < n:
            cum = max(ans[:i]+[0])
            ans[i+d-1] = max(
                ans[i+d-1], cum+p
            )

    print(max(ans))
solution(n, table)
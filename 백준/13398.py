n = int(input())
arr = list(map(int, input().split()))

path = [[0, None] for _ in range(n)]

path[0] = [arr[0], None if arr[0] > 0 else arr[0]]

for i in range(1, n):
    a = arr[i]
    path[i][0] = max(a, path[i-1][0]+a)

    if a < 0: # 음수만 삭제
        b = path[i-1][1]
        
        if b is None: # 이전에 삭제한게 없으면
            path[i][1] = path[i-1][0]
        else: # 삭제한 것이 있으면 max(지금 것을 삭제, 이전 것을 삭제 유지)
            c = max(b+a, path[i-1][0])
            path[i][1] = c
    else:
        if path[i-1][1] is not None:
            path[i][1] = path[i-1][1] + a

max_ = -float('inf')
for a, b in path:
    if a > max_:
        max_ = a
    if b is not None and b > max_:
        max_ = b
print(max_)
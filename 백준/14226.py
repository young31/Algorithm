from collections import deque

n = int(input())

que = deque()
que.append((1, 0, 0))

used = [[False for _ in range(n*10)] for _ in range(n*10)]
while que:
    a, b, c = que.popleft()
    if a-1 > 0 and not used[a-1][c]:
        if a-1 == n:
            print(b+1)
            break
        que.append((a-1, b+1, c))
        used[a-1][c] = True

    if not used[a][a]:
        que.append((a, b+1, a))
        used[a][a] = True

    if not used[a+c][c]:
        if a+c == n:
            print(b+1)
            break
        que.append((a+c, b+1, c))
        used[a+c][c] = True
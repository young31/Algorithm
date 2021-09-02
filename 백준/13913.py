from collections import deque

n, k = map(int, input().split())

# 애초에 빼기만 가능
if k <= n:
    print(n-k)
    print([i for i in range(n, k-1, -1)])
    exit()

visited = [False for _ in range(100000+1)]

que = deque([(n, 0)])
visited[n] = True
history = [-1 for _ in range(100000+1)]

while que:
    cur, c = que.popleft()
    if cur == k:
        print(c)
        path = [k]
        now = k
        while 1:
            before = history[now]
            if before == -1:
                print(*path[::-1])
                exit()
            path.append(before)
            now = before
        break

    if cur <= k:
        if 2*cur < 100001 and not visited[cur*2]:
            que.append((2*cur, c+1))
            visited[cur*2] = True
            history[cur*2] = cur

        if cur+1 < 100001 and not visited[cur+1]:
            que.append((cur+1, c+1))
            visited[cur+1] = True
            history[cur+1] = cur

    if cur-1 >= 0 and not visited[cur-1]:
        que.append((cur-1, c+1))
        visited[cur-1] = True
        history[cur-1] = cur
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trap = {}

for _ in range(n+m):
    a, b = map(int, input().split())
    trap[a] = b

visited = [False for _ in range(101)]
que = deque()
que.append((1, 0))
visited[1] = True
while que:
    cur, c = que.popleft()
    for i in range(1, 7):
        if not visited[cur+i]:
            if cur+i in trap.keys():
                visited[cur+i] = True
                visited[trap[cur+i]] = True
                que.append((trap[cur+i], c+1))

                if trap[cur + i] == 100:
                    print(c+1)
                    exit()
            else:
                visited[cur+i] = True
                que.append((cur+i, c+1))

                if cur + i == 100:
                    print(c+1)
                    exit()
            
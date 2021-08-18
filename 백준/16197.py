from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def is_out(i, j):
    if 0 > i or n <= i:
        return True
    if 0 > j or n <= j:
        return True
    return False

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

n, m = map(int, input().split())


arr = []
coins = []
c = 0
for i in range(n):
    ls = list(input().strip())
    arr.append(ls)
    for j in range(m):
        if ls[j] == 'o':
            coins.append([i, j])
            c += 1

def false(): return False
visited = defaultdict(false)
cc = coins[0]+coins[1]
visited[tuple(cc)] = True

que = deque()
que.append(
    (coins, 0)
)

done = False

while que:
    curs, c = que.popleft()
    if c > 10:
        print(-1)
        exit()
    for di, dj in moves:
        new = []
        cnt = 0
        for idx, (i, j) in enumerate(curs):
            ni = i+di
            nj = j+dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == '.':
                    new.append([ni, nj])
                else:
                    new.append([i, j])
            else:
                cnt += 1

        if cnt == 1:
            if c+1 >= 11:
                print(-1)
            else:
                done = True
                print(c+1)
            exit()
        elif cnt == 0:
            cc = tuple(new[0]+new[1])
            if not visited[cc]:
                visited[cc] = True
                que.append([new, c+1])

if not done:
    print(-1)
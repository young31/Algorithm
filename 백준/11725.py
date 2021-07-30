from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input())

dA = defaultdict(list)
dB = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    dA[a].append(b)
    dB[b].append(a)

que = deque()
que.append(1)

used = [False for _ in range(n+1)]
parents = [x for x in range(n+1)]

while que:
    a = que.popleft()
    used[a] = True
    try:
        xs = dA.pop(a)
        for x in xs:
            if not used[x]:
                parents[x] = a
                que.append(x)
    except:
        ''
    try:
        xs = dB.pop(a)
        for x in xs:
            if not used[x]:
                parents[x] = a
                que.append(x)
    except:
        ''
for p in parents[2:]: print(p)
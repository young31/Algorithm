from collections import deque

def solution(x):
    que = deque([1, 2, 4], maxlen=3)
    if x < 4:
        return que[x-1]
    else:
        k = 3
        while k != x:
            que.append(sum(que))
            k += 1
        return que[-1]

n = int(input())
for _ in range(n):
    q = int(input())
    ans = solution(q)
    print(ans)
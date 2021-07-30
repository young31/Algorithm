n = int(input())
from collections import deque

que = deque(maxlen=2)
que.append(1)
que.append(2)

if n == 1:
    ans = 1
elif n == 2:
    ans = 2
else:
    k = 2
    while k != n: 
        que.append(sum(que)%10007)
        k += 1
    ans = que[-1]

print(ans)
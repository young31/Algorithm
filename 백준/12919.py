from collections import deque

s = input()
t = input()

que = deque()
que.append(t)
done = False

while que:
    t = que.popleft()
    if len(s) == len(t):
        if s == t:
            done = True
    else:
        if t[-1] == 'A':
            que.append(t[:-1])
        if t[0] == 'B':
            que.append(t[::-1][:-1])

if done:
    print(1)
else:
    print(0)
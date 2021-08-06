from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def false(): return False

def op(s, mode):
    if mode == 'D':
        s = (s*2)%10000
    elif mode == 'S':
        if s == 0:
            s = 9999
        else:
            s = s-1
    elif mode == 'L':
        s = s % 1000 * 10 + s // 1000
    elif mode == 'R':
        s = s % 10 * 1000 + s // 10
    return s

def search(a, b):
    que = deque([(a, '')])
    used = defaultdict(false)
    while que:
        s, c = que.popleft()
        for o in ops:
            s_ = op(s, o)
            c_ = c+o
            if s_ == b:
                return c_
            if not used[s_]:
                que.append((s_, c_))
                used[s_] = True

ops = ['D', 'S', 'L', 'R']
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    c = search(a, b)
    print(c)
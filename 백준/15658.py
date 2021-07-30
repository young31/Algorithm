from itertools import permutations
from collections import defaultdict

def do_op(n, op):
    res = n[0]
    for i, o in enumerate(op, 1):
        if o == 0: # +
            res += n[i]
        elif o == 1: # -
            res -= n[i]
        elif o == 2: # x
            res *= n[i]
        else: # /
            if res >= 0:
                res = res // n[i]
            else:
                tmp = abs(res)
                tmp = tmp // n[i]
                res = -tmp
    return res
    
n = int(input())
a = list(map(int, input().split()))
k = len(a)-1
op = list(map(int, input().split()))

ops = []
for i, o in enumerate(op):
    ops += [i for _ in range(o)]
    
res = set()

def search(sub, c):
    global res, op
    if c == k:
        score = do_op(a, sub)
        res.add(score)
    else:
        for i in range(4):
            if op[i] > 0:
                op[i] -= 1
                search(sub+[i], c+1)
                op[i] += 1


search([], 0)
print(max(res))
print(min(res))
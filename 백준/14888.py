from itertools import permutations

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
op = list(map(int, input().split()))

ops = []
for i, o in enumerate(op):
    ops += [i for _ in range(o)]
    
res = set()
for perm in permutations(ops):
    res.add(do_op(a, perm))

print(max(res))
print(min(res))
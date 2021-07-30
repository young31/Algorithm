from collections import defaultdict

def false():
    return False

n = int(input())
arr = list(map(int, input().split()))

has = defaultdict(false)
for a in arr:
    has[a] = True

m = int(input())
is_has = list(map(int, input().split()))

res = []
for i in is_has:
    if has[i]:
        res.append(1)
    else:
        res.append(0) 

print(*res)


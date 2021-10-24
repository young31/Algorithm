from collections import defaultdict
from copy import deepcopy

n, m, k = map(int, input().split())

sharks = {}
for _ in range(k):
    r, c, s, d, z = map(int, input().split())
    sharks[(r-1, c-1)] = (z, s, d)

answer = 0

def move(i, j, s, d):
    if d == 1:
        i -= s
    elif d == 2:
        i += s
    elif d == 3:
        j += s
    elif d == 4:
        j -= s

    if d in [1, 2]:
        i = i % (2*(n-1))
        if i >= n-1:
            if d == 1: d = 2
            elif d == 2: d = 1
        if i > n-1:
            i = 2*(n-1) - i
    
    elif d in [3, 4]:
        j = j % (2*(m-1))
        if j >= m-1:
            if d == 3: d = 4
            elif d == 4: d = 3
        if j > m-1:
            j = 2*(m-1) - j

    return i, j, d

for J in range(m):
    # do
    for i in range(n):
        c = sharks.get((i, J))
        if c is not None:
            answer += c[0]
            sharks.pop((i, J))
            break

    new = {}
    for (i, j), (z, s, d) in sharks.items():
        ni, nj, nd= move(i, j, s, d)
        if new.get((ni, nj)) is not None:
            pz, ps, pd = new[(ni, nj)]
            if pz < z:
                new[(ni, nj)] = (z, s, nd)
        else:
            new[(ni, nj)] = (z, s, nd)
    
    sharks = deepcopy(new)

print(answer)

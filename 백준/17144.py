from collections import defaultdict

moves = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

n, m, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dust = defaultdict(int)
a1 = a2 = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            if a1 == 0:
                a1 = (i, j)
            else:
                a2 = (i, j)
        elif arr[i][j] != 0:
            dust[(i, j)] = arr[i][j]

def move(i, j):
    if i < a1[0] and j == 0:
        i += 1
        if i == a1[0]:
            return None
    elif i == 0:
        j -= 1
    elif i <= a1[0] and j == m-1:
        i -= 1
    elif i == a1[0]:
        j += 1

    elif i > a2[0] and j == 0:
        i -= 1
        if i == a2[0]:
            return None
    elif i == n-1:
        j -= 1
    elif i >= a2[0] and j == m-1:
        i += 1
    elif i == a2[0]:
        j += 1
    return i, j

for _ in range(t):
    near = defaultdict(int)
    for (i, j), v in dust.items():
        nv = v//5
        c = 0
        for di, dj in moves:
            ni = i+di; nj = j+dj
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) != a1 and (ni, nj) != a2:
                near[(ni, nj)] += nv
                c += 1
        dust[(i, j)] -= nv*c

    for (i, j), v in near.items():
        dust[(i, j)] += v

    new = defaultdict(int)
    for (i, j), v in dust.items():
        if j == 0 and i == a1[0]-1:
            continue
        elif j == 0 and i == a2[0]+1:
            continue
        else:
            new[move(i, j)] = v

    dust = new

answer = sum(dust.values())
print(answer)



def get_next(i, j, d):
    if d == 0:
        return i, j-1
    elif d == 1:
        return i-1, j
    elif d == 2:
        return i, j+1
    elif d == 3:
        return i+1, j

def get_rear(i, j, d):
    if d == 0:
        return i+1, j
    elif d == 1:
        return i, j-1
    elif d == 2:
        return i-1, j
    elif d == 3:
        return i, j+1

n, m = map(int, input().split())
i, j, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
while 1:
    if arr[i][j] == 0:
        cnt += 1
        arr[i][j] = 2

    nd = d
    for rot in range(4):
        ni, nj = get_next(i, j, nd)
        nd = (d-rot-1)%4
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
            i = ni
            j = nj
            d = nd
            break
    else:
        ni, nj = get_rear(i, j, d)
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 1:
            i, j = ni, nj 
        else:
            break

print(cnt)

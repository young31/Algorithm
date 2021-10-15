from copy import deepcopy

def cover_one(i, j, h, arr_):
    arr = deepcopy(arr_)
    if h == 0:
        for x in range(i-1, -1, -1):
            if arr[x][j] != 6:
                arr[x][j] = '#'
            else:
                break
    elif h == 1:
        for x in range(j+1, m):
            if arr[i][x] != 6:
                arr[i][x] = '#'
            else:
                break
    elif h == 2:
        for x in range(i+1, n):
            if arr[x][j] != 6:
                arr[x][j] = '#'
            else:
                break
    elif h == 3:
        for x in range(j-1, -1, -1):
            if arr[i][x] != 6:
                arr[i][x] = '#'
            else:
                break
    return arr

def count(arr):
    c = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                c += 1
    return c

def search(i, arr):
    global answer
    if i == len(cams):
        c = count(arr)
        answer = min(c, answer)

    else:
        cam, x, y = cams[i]
        if cam == 1:
            for h in range(4):
                arr_ = cover_one(x, y, h, arr)
                search(i+1, arr_)
        
        elif cam == 2:
            for h in range(2):
                if h == 0:
                    arr_ = cover_one(x, y, 0, arr)
                    arr_ = cover_one(x, y, 2, arr_)
                elif h == 1:
                    arr_ = cover_one(x, y, 1, arr)
                    arr_ = cover_one(x, y, 3, arr_)
                search(i+1, arr_)

        elif cam == 3:
            for h in range(4):
                arr_ = cover_one(x, y, h, arr)
                arr_ = cover_one(x, y, (h+1)%4, arr_)
                search(i+1, arr_)

        elif cam == 4:
            for h in range(4):
                arr_ = cover_one(x, y, h, arr)
                arr_ = cover_one(x, y, (h+1)%4, arr_)
                arr_ = cover_one(x, y, (h-1)%4, arr_)
                search(i+1, arr_)

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')
cams = []
av_cam = [i for i in range(1, 5)]
cam5 = []
for i in range(n):
    for j in range(m):
        if arr[i][j] in av_cam:
            cams.append((arr[i][j], i, j))
        elif arr[i][j] == 5:
            cam5.append((i, j))

for i, j in cam5:
    for h in range(4):
        arr = cover_one(i, j, h, arr)

search(0, arr)
print(answer)
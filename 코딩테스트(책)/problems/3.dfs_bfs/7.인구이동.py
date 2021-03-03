# input
n1, l1, r1 = 2, 20, 50
arr1 = [
    [50, 30],
    [20, 40]
]

n2, l2, r2 = 2, 40, 50
arr2 = [
    [50, 30],
    [30, 40]
]

n3, l3, r3 = 2, 20, 50
arr3 = [
    [50, 30],
    [30, 40]
]

n4, l4, r4 = 3, 5, 10
arr4 = [
    [10, 15, 20],
    [20, 30, 25],
    [40, 22, 10]
]

n5, l5, r5 = 4, 10, 50
arr5 = [
    [10, 100, 20, 90],
    [80, 100, 60, 70],
    [70, 20, 30, 40],
    [50, 20, 100, 10]
]
# answer: 1

# algo
from copy import deepcopy

n, l, r = n5, l5, r5
arr = arr5

move = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]


def grouping(xy, no):
    global groups, group_mean
    x, y = xy
    groups[x][y] = no
    if no in group_mean.keys():
        group_mean[no].append(arr[x][y])
    else:
        group_mean[no] = [arr[x][y]]

    for m in move:
        dx, dy = m
        nx = x+dx
        ny = y+dy
        if 0 <= nx < n and 0 <= ny < n and groups[nx][ny] == 0 and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
            grouping((nx, ny), no)

cnt = 0
while 1:
    no_g = 1
    groups = [[0 for _ in range(n)] for _ in range(n)]
    group_mean = {}
    for i in range(n):
        for j in range(n):
            if groups[i][j] == 0:
                grouping((i, j), no_g)
                no_g += 1

    next_arr = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = round(sum(group_mean[groups[i][j]]) / len(group_mean[groups[i][j]]))

    if arr == next_arr:
        break
    else:
        cnt += 1
        arr = next_arr
    

print(cnt)

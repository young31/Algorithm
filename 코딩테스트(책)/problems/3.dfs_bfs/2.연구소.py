# input
n1, m1 = 7, 7
input1 = [
    [2, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 2, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0]
]

n2, m2 = 4, 6
input2 = [
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 2],
    [1, 1, 1, 0, 0, 2],
    [0, 0, 0, 0, 0, 2]
]

n3, m3 = 8, 8
input3 = [
    [2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
# answer: 27, 9, 3

# algo
## 완전탐색으로 벽을 세울 수 있는 모든 조합을 고려
## 안전지대의 최대값을 구하는 대신 퍼지는 바이러스의 최소값을 찾는 것으로 변형하여 해결

from copy import deepcopy
def comb_loader(arr):
    # 벽을 세울 수 있는 곳을 loading
    n = len(arr)
    m = len(arr[0])
    for i in range(n*m):
        x1, x2 = i//m, i%m
        if not is_feasible_wall(arr, x1, x2):
            continue

        for j in range(i+1, n*m):
            y1, y2 = j//m, j%m
            if not is_feasible_wall(arr, y1, y2):
                continue

            for k in range(j+1, n*m):
                z1, z2 = k//m, k%m
                if not is_feasible_wall(arr, z1, z2):
                    continue

                yield (i, j, k)

def is_feasible_wall(arr, x, y):
    n = len(arr)
    m = len(arr[0])
    if 0 <= x < n and 0 <= y < m and arr[x][y] == 0:
        return True
    return False

def contaminate(arr):
    # 바이러스가 퍼질 수 있는 곳으로 퍼지는 경우 면적
    move = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]
    n = len(arr)
    m = len(arr[0])
    q = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i, j))

    cnt = 0
    while q:
        nq = []
        for i, j in q:
            for m1, m2 in move:
                ni, nj = i+m1, j+m2
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                    arr[ni][nj] = 2
                    nq.append((ni, nj))
                    cnt += 1
        q = nq
    return cnt

def main(n, m, arr):
    # initialize
    n_wall = 0
    n_virus = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                n_wall += 1
            elif arr[i][j] == 2:
                n_virus += 1

    ans = float('inf')
    # 모든 조합 고려
    for i, j, k in comb_loader(arr):
        x1, x2 = i//m, i%m
        y1, y2 = j//m, j%m
        z1, z2 = k//m, k%m

        tmp = deepcopy(arr)
        tmp[x1][x2] = 1
        tmp[y1][y2] = 1
        tmp[z1][z2] = 1
        
        tmp_ans = contaminate(tmp)

        if ans > tmp_ans:
            ans = tmp_ans
    # 변형접근을 원래 방식으로 변환
    return n*m - ans - n_wall - n_virus - 3

print(main(n1, m1, input1))
print(main(n2, m2, input2))
print(main(n3, m3, input3))

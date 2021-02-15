# input
n1, k1 = 3, 3
arr1 = [
    [1, 0, 2],
    [0, 0, 0],
    [3, 0, 0]
]
s1, x1, y1 = 2, 3, 2

n2, k2 = 3, 3
arr2 = [
    [1, 0, 2],
    [0, 0, 0],
    [3, 0, 0]
]
s2, x2, y2 = 1, 2, 2

# answer: 3, 0

# algo
from copy import deepcopy
from pprint import pprint

move = [
    (1, 0), (-1, 0), (0, 1), (0, -1)
]

def main(n, k, s, x, y, arr):
    # 좌표만 저장
    v_map = {}
    for i in range(1, k+1):
        v_map[i] = []

    for i in range(n):
        for j in range(n):
            v = arr[i][j]
            if v != 0:
                v_map[v].append((i, j))

    for e in range(s): # 반복조건
        for v in v_map.keys(): # 작은 바이러스부터 시작
            new_area = [] # 전염되고 나면 기존 좌표는 필요 없으므로 갱신
            for i, j in v_map[v]:
                for di, dj in move:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0: # 전염될 수 있으면 전염
                        arr[ni][nj] = v
                        new_area.append((ni, nj))
    
            v_map[v] = new_area
        # for _ in range(n): print(arr[_])
        # print()
    return arr[x-1][y-1]

print(main(n1, k1, s1, x1, y1, arr1))
print(main(n2, k2, s2, x2, y2, arr2))
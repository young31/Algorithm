# https://programmers.co.kr/learn/courses/30/lessons/60059
# input
key = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]

lock = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
# answer: true

# algo
## 처음에는 감도 안와서 못풀고 있다가 불현듯 다시 풀려니까 아이디어가 떠올랐다.
## 언젠가 카카오 문제였던 듯
## transpose, flip 두 단계로 회전을 줘서 시간이 오래걸릴까 걱정했지만 문제는 없었다.
## 넘파이 등을 사용할 수 있었으면 더 빨랐을 텐데..
from copy import deepcopy
def padding(a, n):
    m = len(a)
    res = [[0 for _ in range(n*2+m)] for _ in range(n)]
    res += [[0]*n + a[i] + [0]*n for i in range(m)]
    res += [[0 for _ in range(n*2+m)] for _ in range(n)]
    return res

def rotate(a, dir):
    if dir == 0:
        return a
    elif dir == 1:
        return horizontal_flip(transpose(a))
    elif dir == 2:
        return horizontal_flip(vertical_flip(a))
    else:
        return vertical_flip(transpose(a))

def horizontal_flip(a):
    res = deepcopy(a)

    n = len(res)
    for i in range(n):
        for j in range(n//2):
            res[i][j], res[i][n-j-1] = res[i][n-j-1], res[i][j]

    return res

def vertical_flip(a):
    res = deepcopy(a)
    n = len(res)
    for i in range(n//2):
        for j in range(n):
            res[i][j], res[n-i-1][j] = res[n-i-1][j], res[i][j]

    return res

def transpose(a):
    res = deepcopy(a)
    n = len(a)
    for i in range(n):
        for j in range(i, n):
            if i != j:
                res[i][j], res[j][i] = res[j][i], res[i][j]
    return res

def match(lock, back, i, j):
    n = len(lock)
    for r in range(n):
        for c in range(n):
            if lock[r][c] + back[i+r][j+c] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    back = padding(key, n-1)

    k = len(back)
    for d in range(4):
        lck = rotate(lock, d)
        for i in range(k-n):
            for j in range(k-n):
                if match(lck, back, i, j):
                    return True

    return False


print(solution(key, lock))

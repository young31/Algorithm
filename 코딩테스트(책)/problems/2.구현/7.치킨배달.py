# input
n1, m1 = 5, 3
arr1 = [
    [0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]
]

n2, m2 = 5, 2
arr2 = [
    [0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]
]

n3, m3 = 5, 1
arr3 = [
    [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0]
]

n4, m4 = 5, 1
arr4 = [
    [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1]
]

# answer: 5, 10, 11, 32

# algo
from copy import deepcopy

def dist(x, y):
    x1, x2 = x
    y1, y2 = y
    return abs(x1-y1) + abs(x2-y2)

def cond_min(x, c):
    ans = float('inf')
    for a, b in zip(x, c):
        if b == 1 and a < ans:
            ans = a
    return ans

def get_min(x, c):
    ans=0
    for s in x:
        ans+=cond_min(s, c)
    return ans

def build_matrix(chicks, houses):
    n = len(houses)
    m = len(chicks)

    mat = [[dist(houses[j], chicks[i]) for i in range(m)] for j in range(n)]

    return mat

def comb(mat, ls, idx, s):
    
    if sum(ls) == s:
        ans = get_min(mat, ls)
        return ans

    elif idx >= len(ls):
        return float('inf')

    ls[idx] = 0
    l1=deepcopy(ls)
    ls[idx] = 1
    l2=deepcopy(ls)
    
    res = min(comb(mat, l1, idx+1, s),comb(mat, l2, idx+1, s))

    return res

def main(n, m, arr):
    chicks = []
    houses = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                houses.append((i, j))
            elif arr[i][j] == 2:
                chicks.append((i, j))

    mat=build_matrix(chicks, houses)

    ans=999
    ls=[0 for _ in range(len(chicks))]
    print(comb(mat, ls, 0, m))

main(n1,m1,arr1)
main(n2,m2,arr2)
main(n3,m3,arr3)
main(n4,m4,arr4)
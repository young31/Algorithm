from copy import deepcopy

def check(i, j, arr):
    cA = 0
    cB = 0
    for di in range(8):
        for dj in range(8):
            ni = i+di
            nj = j+dj
            if arr[ni][nj] != template_a[di][dj]:
                cA += 1
            if arr[ni][nj] != template_b[di][dj]:
                cB += 1
    
    return min(cA, cB)


n, m = map(int, input().split())

arr = [
    input() for _ in range(n)
]

template_a = [
    'WB'*4, 'BW'*4,'WB'*4, 'BW'*4,'WB'*4, 'BW'*4,'WB'*4, 'BW'*4,
]

template_b = [
    'BW'*4, 'WB'*4, 'BW'*4,'WB'*4, 'BW'*4,'WB'*4, 'BW'*4, 'WB'*4,
]

score = float('inf')
for i in range(0, n-7):
    for j in range(0, m-7):
        score = min(score, check(i,j,arr))

print(score)
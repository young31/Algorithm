from copy import deepcopy

def rotation(x, d):
    if d == -1:
        return x[1:] + [x[0]]
    elif d == 1:
        return [x[-1]] + x[:-1]

casts = [
    list(map(int, list(input()))) for _ in range(4)
]

k = int(input())

for _ in range(k):
    s, D = map(int, input().split())
    d = D

    new_casts = deepcopy(casts)
    new_casts[s-1] = rotation(casts[s-1], D)

    for i in range(s-1, 3):
        if casts[i][2] != casts[i+1][-2]:
            if d == -1:
                new_casts[i+1] = rotation(casts[i+1], 1)
                d = 1
            elif d == 1:
                new_casts[i+1] = rotation(casts[i+1], -1)
                d = -1
        else:
            break
    
    d = D
    for i in range(s-1, 0, -1):
        if casts[i][-2] != casts[i-1][2]:
            if d == -1:
                new_casts[i-1] = rotation(casts[i-1], 1)
                d = 1
            elif d == 1:
                new_casts[i-1] = rotation(casts[i-1], -1)
                d = -1
        else:
            break

    casts = deepcopy(new_casts)

answer = 0
for i in range(4):
    answer += (2**i)*casts[i][0]
print(answer)
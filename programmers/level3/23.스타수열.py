a = [0,3,3,0,7,2,0,2,2,0]

from collections import defaultdict, deque

def check(a, x, i, dct):
    n = len(a)
    if i == 0:
        if a[1] != x:
            dct.append(1)
            return 2
    elif i == n-1:
        if (a[i-1] != x and i-1 not in dct):
            dct.append(i-1)
            return 2
    else:
        if (a[i-1] != x and i-1 not in dct[-3:]):
            dct.append(i-1)
            return 2
        elif (a[i+1] != x):
            dct.append(i+1)
            return 2
    return 0

def solution(a):
    if len(a) == 1:
        return 0
    
    answer = 0
    
    dct = defaultdict(list)
    scores = defaultdict(int)
    for i, s in enumerate(a):
        dct[s].append(i)
        scores[s] += check(a, s, i, dct[s])

    answer = max(scores.values())
    print(answer)
    return answer

solution(a)
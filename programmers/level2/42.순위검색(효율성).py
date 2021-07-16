info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from itertools import product
from collections import defaultdict
import heapq
import bisect

def solution(info, query):
    answer = []

    storage = defaultdict(list)
    for inf in info:
        l, e, ex, f, s = inf.split(' ')
        for p in product([l, ''], [e, ''], [ex, ''], [f, '']):
            new = ''.join(p)
            heapq.heappush(storage[new], int(s))

    for q in query:
        l, e, ex, fs = list(map(lambda x: x.replace('-', ''), q.split(' and ')))
        f, s = fs.split(' ')
        new = l+e+ex+f
        # heapq.(storage[new])
        storage[new].sort()
        print(new, s)
        print(storage[new])
        
        if not storage[new]:
            answer.append(0)
        
        elif len(storage[new]) == 1:
            if storage[new][0] >= int(s):
                answer.append(1)
            else:
                answer.append(0)

        else:
            # cnt = len(list(filter(lambda x: x>=int(s), storage[new])))
            l = 0
            r = len(storage[new])-1
            while l <= r:
                mid = (l+r)//2
                if storage[new][mid] >= int(s):
                    cnt = len(storage[new])- mid
                    r = mid-1
                else:
                    l = mid+1

            answer.append(cnt)
        print(answer[-1])
        print()

    print(answer)
    return answer

def solution(info, query):
    answer = []
    storage = {}

    for q in query:
        l, e, ex, fs = list(map(lambda x: x.replace('-', ''), q.split(' and ')))
        f, s = fs.split(' ')
        new = l+e+ex+f
        storage[new] = []

    for inf in info:
        l, e, ex, f, s = inf.split(' ')
        for p in product([l, ''], [e, ''], [ex, ''], [f, '']):
            new = ''.join(p)
            if new in storage.keys():
                heapq.heappush(storage[new], int(s))
    
    for q in query:
        l, e, ex, fs = list(map(lambda x: x.replace('-', ''), q.split(' and ')))
        f, s = fs.split(' ')
        new = l+e+ex+f
        print(storage[new])

        cnt = len(list(filter(lambda x: x >= int(s), storage[new])))
        answer.append(cnt)

        for _ in range(len(storage[new])):
            print(heapq.heappop(storage[new]))

    print(answer)
    return answer

solution(info, query)
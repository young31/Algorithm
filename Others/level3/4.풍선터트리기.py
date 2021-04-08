a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
# a = [9,-1,-5]

import heapq

def solution(a):
    if len(a) <= 2:
        return len(a)

    answer = 2
    indices = []
    for i, t in enumerate(a):
        heapq.heappush(indices, (t, i))

    _, i1 = heapq.heappop(indices)
    _, i2 = heapq.heappop(indices)
    i1, i2 = max(i1, i2), min(i1, i2)
    while indices:
        _, i = heapq.heappop(indices)
        if i > i1:
            i1 = i
            answer += 1
        elif i < i2:
            i2 = i
            answer += 1

    print(answer)
    return answer

solution(a)
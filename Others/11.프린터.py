priorities = [2, 1, 3, 2]
location = 2

priorities = [1, 1, 9, 1, 1, 1]
location = 0

from collections import Counter

def solution(priorities, location):
    count = Counter(priorities)
    prior = [(p, i) for i, p in enumerate(priorities, 0)]

    keys = sorted(count.keys(), reverse=True)

    cnt = 1
    for k in keys:
        for _ in range(count[k]):
    
            idx = priorities.index(k)
            if prior[idx][1] == location:
                return cnt
            else:
                prior = prior[idx+1:] + prior[:idx]
                priorities = priorities[idx+1:] + priorities[:idx]
                cnt += 1

print(solution(priorities, location))
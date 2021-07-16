orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    n = len(orders)
    combs = defaultdict(int)

    for i in range(n):
        for j in range(i+1, n):
            a = orders[i]
            b = orders[j]
            s = set(a).intersection(set(b))
            print(s, a, b)
            if len(s) >= 2:
                for k in range(2, len(s)+1):
                    for c in combinations(s, k):
                        new = ''.join(sorted(c))
                        # print(new)
                        combs[new] += 1
            print(combs)
            print()
    print(combs)

    return answer

def solution(orders, course):
    answer = []
    n = len(orders)
    combs = defaultdict(int)

    for o in orders:
        l = len(o)
        for i in range(2, l+1):
            for c in combinations(o, i):
                new = ''.join(sorted(c))
                combs[new] += 1

    tags = defaultdict(list)
    for c, v in combs.items():
        if v < 2:
            continue
        l = len(c)
        if l in course:
            if not tags[l]:
                tags[l].append(c)
            else:
                if combs[tags[l][-1]] < v:
                    tags[l] = [c]
                elif combs[tags[l][-1]] == v:
                    tags[l].append(c)

    print(combs)
    for t in tags.values():
        answer += t
    answer.sort()
    print(answer)
    return answer

solution(orders, course)
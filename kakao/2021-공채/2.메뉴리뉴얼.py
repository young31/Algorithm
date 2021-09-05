from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    menus = {i: defaultdict(int) for i in course}
    for order in orders:
        for c in course:
            for comb in combinations(order, c):
                s = ''.join(sorted(comb))
                menus[c][s] += 1
    
    answer = []
    for c in course:
        if len(menus[c]) == 0:
            continue
        max_ = max(menus[c].values())
        if max_ <= 1:
            continue
        for k, v in menus[c].items():
            if v == max_:
                answer.append(k)
    answer = sorted(answer)
    return answer

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

solution(orders, course)
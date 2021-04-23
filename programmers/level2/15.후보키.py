relation = [["ab", "c"], ["a", "bc"], ["x", "yz"], ["x", "c"]]

from itertools import combinations

def check_unique(relation, cols):
    n = len(relation)

    u = list(map(lambda x: '-'.join([x[c] for c in cols]), relation))
    print(u, set(u))
    if len(set(u)) == n:
        return True
    return False

def check_min(used, cols):
    for u in used:
        if len(set(u).intersection(cols)) == len(set(u)):
            return False
    return True

def solution(relation):
    p = len(relation[0])
    n = len(relation)
    answer = 0

    used = []
    for i in range(1, p+1):
        for comb in combinations(range(p), i):
            # print(comb)
            if check_min(used, comb) and check_unique(relation, comb):
                used.append(comb)

    answer = len(used)
    print(answer)
    return answer

solution(relation)
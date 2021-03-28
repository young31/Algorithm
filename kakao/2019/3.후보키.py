# 실패
# input
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

# answer: 2

# algo
from itertools import combinations
def minimality(x, na):
    total_res = 0
    for n in na:
        res = 1
        for i in n:
            if i in x:
                res *= 1
            else:
                res *= 0 
        if res == 1:
            return True
    return False

from itertools import combinations
def minimality(x, na):
    for n in na:
        # print(set(n), set(x), (set(n) & set(x)))
        if (set(n) & set(x)) == set(n):
            return True
    return False

def uniqueness(relation, cols):
    tmp = []
    for rel in relation:
        r = ''
        for col in cols:
            r += rel[col]
        if r not in tmp:
            tmp.append(r)

    if len(relation) == len(tmp):
        return True
    return False


def solution(relation):
    n = len(relation[0])
    m = len(relation)

    na = []
    for c in range(1, n+1):
        for ls in combinations(range(n), c):
            if not minimality(ls, na) and uniqueness(relation, ls):
                na.append(ls)

    answer = max(list(map(lambda x: len(x), na)))
    return answer

print(solution(relation))
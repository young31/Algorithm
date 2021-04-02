# input
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

# answer: 3

# algo
from itertools import product

def is_match(a, b):
    if len(a) != len(b):
        return False

    for x, y in zip(a, b):
        if y == '*':
            continue
        else:
            if x == y:
                continue
            else:
                return False
    return True

def solution(user_id, banned_id):
    possible = []
    answer = 0
    for b in banned_id:
        tmp = []
        for u in user_id:
            if is_match(u, b):
                tmp.append(u)
        possible.append(tmp)
    print(possible)

    res = []
    for a in product(*possible):
        if len(a) == len(set(a)) and set(a) not in res:
            answer += 1
            res.append(set(a))
    print(answer)
    return answer

solution(user_id, banned_id)
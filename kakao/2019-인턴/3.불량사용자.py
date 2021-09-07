# solution 1
from itertools import product

def solution(user_id, banned_id):
    banned = []
    for b_id in banned_id:
        banned.append([])
        for user in user_id:
            if len(user) != len(b_id):
                continue
            else:
                is_find = True
                for a, b in zip(user, b_id):
                    if b == '*':
                        continue
                    elif a == b:
                        continue
                    else:
                        is_find = False
                        break
                if is_find:
                    banned[-1].append(user)

    answer = []
    for prod in product(*banned):
        if set(prod) not in answer and len(set(prod)) == len(banned):
            answer.append(set(prod))
    return len(answer)

# solution 2
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

    res = []
    for a in product(*possible):
        if len(a) == len(set(a)) and set(a) not in res:
            answer += 1
            res.append(set(a))

    return answer
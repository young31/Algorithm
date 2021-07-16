info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from itertools import product
from collections import defaultdict
import heapq
import bisect

def solution(info, query):
    answer = []
    langs = defaultdict(list)
    fbs = defaultdict(list)
    jss = defaultdict(list)
    pcs = defaultdict(list)
    scores = {}

    for i, inf in enumerate(info):
        (cjp, fb, js, pc, s) = inf.split(' ')
        langs[cjp].append(i)
        fbs[fb].append(i)
        jss[js].append(i)
        pcs[pc].append(i)
        scores[i] = int(s)

    tidx = set(range(len(info)))
    for que in query:
        cjp, fb, js, pc = que.split('and')
        cjp, fb, js, pc = cjp.strip(), fb.strip(), js.strip(), pc.strip()
        pc, s = pc.split(' ')

        idx = tidx.copy()

        if cjp != '-':
            idx = idx.intersection(set(langs[cjp]))
        if fb != '-':
            idx = idx.intersection(set(fbs[fb]))
        if js != '-':
            idx = idx.intersection(set(jss[js]))
        if pc != '-':
            idx = idx.intersection(set(pcs[pc]))

        answer.append(len(list(filter(lambda x: scores[x] >= int(s), idx))))


    print(answer)
    return answer


solution(info, query)
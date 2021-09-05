from itertools import combinations
from collections import defaultdict

def update(i, d, tree):
    while i <= 100000:
        tree[i] += d
        i += (i & -i)

def tree_sum(i, tree):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

def interval_sum(a, tree, b=100000):
    return tree_sum(b, tree) - tree_sum(a-1, tree)

def ls(): return [0 for _ in range(100001)]
def solution(info, query):
    # cols = ['lang', 'fb', 'js', 'cp']
    table = defaultdict(ls)

    for inf in info:
        l, f, j, c, score = inf.split(' ')
        for i in range(1, 5):
            for comb in combinations([l, f, j, c], i):
                s = ''.join(comb)
                update(int(score), 1, table[s])
        update(int(score), 1, table[''])

    answer = []
    for q in query:
        q = q.replace('-', '')
        l, f, j, cs = q.split('and ')
        c, s = cs.split(' ')
        qy = l.strip() + f.strip() + j.strip() + c.strip()
        answer.append(interval_sum(int(s), table[qy]))
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)



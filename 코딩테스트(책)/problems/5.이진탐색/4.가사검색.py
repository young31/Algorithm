# input
w = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
q = ['fro??', '????o', 'fr???', 'fro??', 'pro?']
# answer: [3, 2, 4, 1, 0]

# algo
# 정규표현식을 사용하여 풀면 3개의 효율성에서 통과하지 못했다.
import re

def search(w, q):
    n = len(w)
    q = q.replace('?', '.')
    q = '^'+q+'$'
    res = list(map(lambda x: re.match(q, x), w))
    return n - res.count(None)

def solution(words, queries):
    res = []
    for i, q in enumerate(queries):
        if q in queries[:i]:
            idx = queries.index(q)
            res.append(res[idx])
        else:
            res.append(search(words, q))

    # res = list(map(lambda x: search(words, x), queries))
    print(res)

solution(w, q)

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

import heapq

def solution(genres, plays):
    answer = []
    gen_dct = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in gen_dct.keys():
            gen_dct[g] = []
        # heapq.heappush(gen_dct[g], (-p, i))
        gen_dct[g].append((-p, i))

    for k in gen_dct.keys():
        gen_dct[k] = sorted(gen_dct[k])

    keys = sorted(gen_dct.keys(), key=lambda x: sum([p[0] for p in gen_dct[x]]))
    for k in keys:
        for i in range(min(2, len(gen_dct[k]))):
            answer.append(gen_dct[k][i][1])

    print(answer)
    return answer

solution(genres, plays)
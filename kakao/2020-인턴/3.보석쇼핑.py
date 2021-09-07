# solution 1
from collections import defaultdict
def solution(gems):
    gem_names = set(gems)
    # cnt = {i: 0 for i in gem_names}
    cnt = defaultdict(int)
    key_map = {x: i for i, x in enumerate(gem_names)}
    s = 0
    e = len(gem_names)-1
    for i in range(s, e+1):
        cnt[gems[i]] += 1
    lens = float('inf')
    while s <= e <= len(gems):
        if s-e > lens:
            cnt[gems[s]] -= 1
            s += 1

        if len(cnt) < len(gem_names):
            e += 1
            if e+1 <= len(gems):
                cnt[gems[e]] += 1
            else:
                break
        else:
            if e-s < lens:
                answer = [s+1, e+1]
                lens = e-s
            cnt[gems[s]] -= 1
            if cnt[gems[s]] == 0:
                cnt.pop(gems[s])
            s += 1

    return answer

# solution 2
def solution(gems):
    gem_set = set(gems)
    lens = len(gem_set)
    gem_dct = {k: i for i, k in enumerate(gem_set)}

    l = 0
    r = lens-1
    n = len(gems)
    answer = [l+1, n]
    cnt = [0 for _ in range(len(gem_dct))]
    for i in range(l, r+1):
        cnt[gem_dct[gems[i]]] += 1

    PHASE2 = False
    while l <= r:        
        if l >= n-lens+1:
            break

        if 0 not in cnt:
            PHASE2 = True
            while 0 not in cnt:
                if answer[1] - answer[0] > r-l:
                    answer = [l+1, r+1]
                cnt[gem_dct[gems[l]]] -= 1
                l += 1

        else:
            if r >= n-1:
                for _ in range(r-l-lens+1):
                    if 0 not in cnt:
                        if answer[1] - answer[0] > r-l:
                            answer = [l+1, r+1]
                    cnt[gem_dct[gems[l]]] -= 1
                    l += 1
                break
            elif PHASE2:
                r += 1
                cnt[gem_dct[gems[r]]] += 1
                cnt[gem_dct[gems[l]]] -= 1
                l += 1
            else:    
                while 0 in cnt and r < n-1:
                    r += 1
                    cnt[gem_dct[gems[r]]] += 1

    return answer
# input
gems = ["AA", "AB", "AC", "AA", "AC"]
# answer: 

# algo
from collections import Counter

def solution(gems):
    # cnt_dct = Counter(gems)
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

    print(answer)
    return answer

solution(gems)
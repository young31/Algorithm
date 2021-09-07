def check(stones, k, cut):
    c = 0
    for s in stones:
        if s <= cut:
            c += 1
        else:
            c = 0
        if c >= k:
            return False
    return True   

def solution(stones, k):
    s = 0
    e = max(stones)
    while s <= e:
        mid = (s+e)//2
        if check(stones, k, mid):
            s = mid+1
        else:
            e = mid-1
    return e+1

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3
print(solution(stones, k))

def check(stones, k, mid):
    cnt = 0
    hop = 0
    for s in stones:
        if s < mid:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0

    return True

def solution(stones, k):
    max_ = max(stones)
    if len(stones) <= k:
        return max_

    s = 1
    e = max_
    while s <= e:
        mid = (s+e)//2
        if check(stones, k, mid):
            s = mid+1
        else:
            e = mid-1
    return e
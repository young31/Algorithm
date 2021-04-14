strs = ["app","ap","p","l","e","ple","pp"]
t = "apple"
# strs = ["ba","an","nan","ban","n"]
# t = "banana"
# strs = ["ba","an","nan","n"]
# t = "banana"

# BFS는 시간 초과 => DP로 해결
import heapq

def solution(strs, t):
    if t in strs:
        return 1
    dct = {}
    for s in strs:
        if s[0] not in dct.keys():
            dct[s[0]] = []
        dct[s[0]].append(s)

    answer = 0
    que = []
    init = t[0]
    for v in dct[init]:
        l = len(v)
        if v == t[:l]:
            heapq.heappush(que, (1, -l, v))

    while que:
        print(que)
        i, _, s = heapq.heappop(que)
        l = len(s)
        target = t[l]
        if target in dct.keys():
            for v in dct[target]:
                l2 = len(v)
                if v == t[l:l+l2]:
                    if s+v == t:
                        return i+1
                    heapq.heappush(que, (i+1, -l2-l, s+v))

    return -1

def solution(strs, t):
    if t in strs:
        return 1
    answer = 0
    n = len(t)
    inf = float('inf')
    dp = [inf]*n

    for i in range(5):
        if t[:i+1] in strs:
            dp[i] = 1
    print(dp)
    for i in range(n):
        for k in range(4, -1, -1):
            if i-k < 0:
                continue
            l = i-k
            
            if t[l:i+1] in strs:
                if dp[l-1] == inf:
                    continue
                    dp[i] = 1
                else:
                    dp[i]=min(dp[i], dp[l-1]+1)
                print(l, t[l:i+1])
                print(dp)
        print()
    print(dp)
    if dp[-1] == inf:
        return -1
    else:
        return dp[-1]
    return answer

print(solution(strs, t))
n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]

# n = 200
# weak = [0, 10, 50, 80, 120, 160]
# dist = [1, 10, 5, 40, 30]

from collections import deque

def search(w_, d_):
    w = w_.copy()
    d = d_.copy()
    n = len(w)
    used = [False]*n

    cnt = 0
    i = 0
    j = 1
    while j < n and d:
        if w[j] - w[i] > max(d):
            
            for k in d:
                if k >= w[j-1] - w[i]:
                    break
            d.remove(k)
            cnt += 1
            for k in range(i, j):
                used[k] = True
            i = j
            j = i+1

        elif j == n-1:
            for k in d:
                if k >= w[j] - w[i]:
                    break
            d.remove(k)
            cnt += 1
            for k in range(i, j+1):
                used[k] = True
            i = j
            j = i+1

        else:
            j += 1

    if all(used):
        return True, cnt
    elif n - sum(used) <= len(d):
        return True, cnt+n - sum(used)
    else:
        return False, float('inf')

def solution(n, weak, dist):
    answer = float('inf')
    l = len(weak)
    weak = deque(weak)
    for _ in range(l):
        k = weak.popleft()
        weak.append(k+n)
        
        b, c = search(weak, dist)
        if b:
            if answer > c:
                answer = c
    if answer == float('inf'):
        answer = -1
    return answer

solution(n, weak, dist)
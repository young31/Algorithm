n = 2
times = [1, 2]
# n = 6
# times = [7,10]

def check(n, times):
    answer = 0
    for t in times:
        answer += n//t
    return answer

def solution(n, times):
    answer = 0
    l = 0
    r = int(1e19)

    while l<=r:
        mid = (l+r)//2
        p = check(mid, times)
        print(l, r, mid)
        # answer = mid
        if p == n:
            if check(mid, times) >= n and check(mid-1, times)<n:
                # print('EE', check(mid-1, times))
                return mid
            else:
                r = mid
                continue

        if p > n:
            answer = mid
            r = mid-1
        else:
            l = mid+1
    
    # if answer == 0:
    #     return l
    return answer

print(solution(n, times))
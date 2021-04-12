distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

# distance = 16
# rocks = [4, 8, 11]
# n = 2

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    l = 1
    r = distance
    while l <= r:
        mid = (l+r)//2 # 돌 간의 거리를 이 값 밑으로 맞춤
        # print(mid)
        s = 0
        cnt = 0
        m = float('inf')
        for rock in rocks:
            if rock - s < mid: # mid보다 작으면 파괴할 수 있음
                cnt += 1 # 파괴한 돌 수
                if cnt > n: # 파괴를 더 많이함 => mid 값을 낮춰도 됨
                    break
            else:
                m = min(m, rock-s) # 못 부수는 경우에 최소값을 갱신
                s = rock
        
        if cnt > n:
            r = mid-1
        else:
            answer = m
            l = mid+1

    print(answer)
    return answer


solution(distance, rocks, n)
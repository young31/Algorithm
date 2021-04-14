works = [2, 1, 2]
n = 1

# works = [4, 3, 3]
# n = 4

# 이진으로 target구해야 될 줄 알고, 일부로 그쪽으로 갔는데
# 그냥 최대 값 평탄화만 해줘도 충분함
import heapq

def solution(n, works):
    if sum(works) < n:
        return 0
    answer = 0
    hw = []
    for w in works:
        heapq.heappush(hw, -w)

    while n > 0:
        cur = heapq.heappop(hw)
        heapq.heappush(hw, cur+1)
        n -= 1

    for w in hw:
        answer += w**2
    return answer

solution(n, works)
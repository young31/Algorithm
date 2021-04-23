scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    if len(scoville) == 1:
        if scoville[0] < K:
            return -1
        else:
            return 0

    while 1:
        if len(scoville) == 1:
            if scoville[0] >= K:
                break
            else:
                answer = -1
                break

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a < K or b < K:
            c = a+2*b
            heapq.heappush(scoville, c)
            answer += 1

        if not scoville:
            break

    print(answer)
    return answer

solution(scoville, K)
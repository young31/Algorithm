# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
# input
food_times = [3, 1, 2]
k = 5

# answer: 1

# algo
## 프로그래머스 문제
## 정확성은 다 맞는데 효율성은 통과하기가 힘들다..
def solution(food_times, k):
    ft = food_times
    total = sum(ft)

    if total <= k:
        return -1

    non_zero = [(s, i) for i, s in enumerate(ft, 1) if s != 0]

    while 1:
        # print(non_zero)
        if k < len(non_zero):
            return non_zero[k][1]
        
        if min(non_zero)[0] > k:
            return non_zero[k%len(non_zero)][1]

        c = max(1, min(non_zero)[0]-1)
        k -= len(non_zero)*c
        non_zero = [(s-c, i) for s, i in non_zero if s-c != 0]
        

# def solution(food_times, k):
#     import heapq
#     ft = food_times
#     total = sum(ft)
#     cnt = len(ft)

#     if total <= k:
#         return -1

#     q = []
#     for i, f in enumerate(ft, 1):
#         heapq.heappush(q, (f, i))

#     sum_v = 0; prev_v = 0
    
#     length = len(ft)
    
#     while sum_v + (q[0][0] - prev_v)*length <= k:
#         now = heapq.heappop(q)[0]
#         sum_v += (now - prev_v) * length
        
#         length -= 1
#         prev_v = now
        
#     res = sorted(q, key = lambda x: x[1])
#     return res[(k-sum_v) % length][1]


print(solution(food_times, k))


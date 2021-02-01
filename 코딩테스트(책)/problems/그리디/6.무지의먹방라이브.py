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

        # if len(non_zero)==0:
        #     return -1

print(solution(food_times, k))

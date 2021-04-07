prices = [1, 2, 3, 2, 3]

def solution(prices):
    n = len(prices)
    answer = [0]*n
    for i, p in enumerate(prices):
        cnt = 0
        for j in range(i+1, n):
            if prices[j] >= p:
                cnt += 1
                answer[i] = cnt
            else:
                answer[i] = cnt+1
                break

    print(answer)
    return answer

solution(prices)
money = [1, 2, 3, 1]
money = [11, 10, 5, 7, 5, 7]
# money = [11, 0, 0, 0, 10, 3]
# money = [1, 1, 4, 1, 4]

def solution(money):
    answer = 0
    n = len(money)
    dp1 = [money[0], money[0]]
    dp2 = [0, money[1]]

    for i in range(2, n-1):
        dp1.append(max(dp1[i-2]+money[i], dp1[i-1]))
    
    for i in range(2, n):
        dp2.append(max(dp2[i-2]+money[i], dp2[i-1]))

    print(dp1)
    print(dp2)
    answer = max(max(dp1), max(dp2))
    print(answer)
    return answer

solution(money)
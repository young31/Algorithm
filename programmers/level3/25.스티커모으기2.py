sticker = [1, 3, 2, 5, 4]

# level4 도둑질과 같은 문제

def solution(sticker):
    answer = 0
    n = len(sticker)
    if n <= 2:
        return max(sticker)

    dp1 = [sticker[0], sticker[0]]
    dp2 = [0, sticker[1]]

    for i in range(2, n-1):
        dp1.append(max(dp1[i-2]+sticker[i], dp1[i-1]))
    
    for i in range(2, n):
        dp2.append(max(dp2[i-2]+sticker[i], dp2[i-1]))
    
    answer = max(max(dp1), max(dp2))
    print(dp1, dp2)
    print(answer)
    return answer

solution(sticker)
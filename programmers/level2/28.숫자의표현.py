def solution(n):
    answer = 0
    ls = list(range(1, n+1))
    for i in range(1, n+1):
        j = 1
        while j <= n-i:
            s = sum(ls[i:i+j])
            if s == n:
                answer += 1
                break
            elif s > n:
                break 
            else:
                j += 1
    print(answer)

    return answer
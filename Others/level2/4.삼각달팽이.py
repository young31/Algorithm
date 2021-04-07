n = 7

def solution(n):
    answer = []
    top = {e: [False]*e for e in range(1, n+1)}
    top[1][0] = 1

    q = n
    m = 0
    while q > 0:
        print(q)
        for i in range(m+2, n+1-m):
            if not top[i][m]:
                top[i][m] = top[i-1][m]+1

        for k in range(1, n-m):
            if not top[i][k]:
                top[i][k] = top[i][k-1]+1

        for i in range(n-1, m+1, -1):
            if not top[i][-m-1]:
                top[i][-m-1] = top[i+1][-m-1]+1

        m += 1
        q -= 3
        print(top)
    for v in top.values():
        answer += v
    print(top)
    print(answer)
    return answer

solution(n)
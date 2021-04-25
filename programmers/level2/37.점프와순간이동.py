n = 1000000000-1
n = 1

def solution(n):
    ans = 0

    if n==1:
        return 1

    while 1:
        if n%2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1
        
        if n == 1:
            ans += 1
            break
    print(ans)
    return ans

solution(n)
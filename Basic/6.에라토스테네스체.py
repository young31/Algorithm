# 소수를 찾고 배수를 지워가면서 구간 내 소수를 찾는 방법
def getPrime(n):
    arr = list(range(n+1))
    res = []
    for i in range(2, n+1):
        if arr[i] != 0: # 삭제를 0으로 처리
            res.append(i)
            for j in range(2*i, n+1, i):
                arr[j] = 0
    return res

print(getPrime(1000))
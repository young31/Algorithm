n = 4
k = 14

def facto(n):
    if n <= 2:
        return n
    return facto(n-1)*n

def solution(n, k):
    answer = []
    arr = list(range(1, n+1))

    i = 1
    c = 0
    for _ in range(n):
        m = facto(n-i)
        for j in range(n-i+1):
            if k <= c+m:
                i += 1
                answer.append(arr[j])
                arr.pop(j)
                break
            else:
                c +=m 
    answer += arr
    print(answer)
    return answer

solution(n, k)
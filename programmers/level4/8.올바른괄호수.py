# 카탈란 수라는 것을 알면 쉽게 풀 수도 있으나.. 모른 상태로도 해결 할 수 있다.

def count(arr, i, k, n):
    global cnt
    # ( 를 앞에서 부터 차례로 쓰고
    # ) 와 바꿀 수 있는 경우를 count한다.
    # 이 때 ) 전의 ( 수는 많거나 같아야 한다.
    # -1: ) // 1: ( 을 의미
    if len(arr) == n:
        if i == k:
            cnt += 1
        return

    if sum(arr) > 0:
        if i < k:
            count(arr+[-1], i+1, k, n) 
        count(arr+[1], i, k, n) 
        
    
    else:
        count(arr+[1], i, k, n)

def solution(n):
    global cnt
    answer = 0
    m = n//2+1
    for i in range(m):
        cnt = 0
        count([1], 0, i, n)
        answer += cnt**2
    print(answer)
    return answer

cnt = 0

for p in range(1, 6):
    solution(p)
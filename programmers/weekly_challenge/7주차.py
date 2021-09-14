def solution(enter, leave):
    n = len(enter)
    answer = [0 for _ in range(n+1)]
    e = 0
    l = 0   
    q1 = []
    while 1:
        if leave[l] not in q1:
            answer[enter[e]] += len(q1)
            for q in q1:
                answer[q] += 1
            q1.append(enter[e])
            e += 1
        else:
            q1.remove(leave[l])
            l += 1

        if e >= n and l >= n:
            break
        
    return answer[1:]

enter = [1,4,2,3]
leave = [2,1,3,4]
print(solution(enter, leave))
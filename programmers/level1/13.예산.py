def solution(d, budget):
    d.sort()
    
    tmp = 0
    for i, v in enumerate(d):
        tmp += v
        if tmp > budget:
            answer = i
            break
    else:
        answer = len(d)
    return answer
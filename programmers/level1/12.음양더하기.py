def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        s = 2*s-1
        answer += a*s
    return answer
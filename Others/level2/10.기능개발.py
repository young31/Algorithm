progresses = [93, 30, 55]
speeds = [1, 30, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    import math
    answer = []
    idx = 0
    while idx < len(progresses):
        nxt = progresses[idx]
        dur = math.ceil((100 - nxt)/speeds[idx])
        for i, p in enumerate(progresses[idx:], 1):
            if p + speeds[idx+i-1]*dur >= 100:
                continue
            else:
                i -= 1
                break
        idx += i
        answer.append(i)
    
    print(answer)
    return answer

solution(progresses, speeds)
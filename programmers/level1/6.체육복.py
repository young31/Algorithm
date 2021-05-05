n = 5
lost = [2,4]
reserve = [2, 3, 5]

from collections import defaultdict

def solution(n, lost, reserve):
    answer = n - len(lost)
    used = {}
    lost.sort()
    reserve.sort()
    for l in lost:
        used[l] = False

    for r in reserve:
        if r in used.keys():
            used[r] = True
            # answer += 1
            continue

        if r-1 in used.keys() and not used[r-1]:
            used[r-1] = True
            # answer += 1
            continue

        if r+1 in used.keys() and not used[r+1]:
            used[r+1] = True
            # answer += 1
            continue

    answer = n + len(used) - sum(used.values())

    print(answer)
    return answer

solution(n, lost, reserve)
# input
n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

# answer: [3, 4, 2, 1, 5]

# algo
from collections import Counter
def solution(n, stages):
    count =  Counter(stages)

    users = {}
    n_user = 0
    total = len(stages)
    for i in range(1, n+1):
        users[i] = total - n_user
        n_user += count[i]

    answer = sorted(list(users.keys()), key=lambda x: (-count[x]/(users[x]), x) if users[x] != 0 else (0, x))
    return answer

print(solution(n, stages))
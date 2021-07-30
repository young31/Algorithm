from copy import deepcopy

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

best = float('inf')
for i in range(3): # 첫 번째는 하나씩 선택해보며
    costs_ = deepcopy(costs)
    costs_[0] = [float('inf') for _ in range(3)]
    costs_[0][i] = costs[0][i]

    for j in range(1, n):
        # 이 전 선택에 따른 현재 최적 선택 값
        costs_[j][0] += min(costs_[j-1][1], costs_[j-1][2])
        costs_[j][1] += min(costs_[j-1][0], costs_[j-1][2])
        costs_[j][2] += min(costs_[j-1][0], costs_[j-1][1])

    costs_[-1][i] = float('inf')
    best = min(min(costs_[-1]), best)
print(best)
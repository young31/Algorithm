from itertools import permutations

n = int(input())
target = list(map(int, input().split()))
flag = False

if n == 1:
    print(-1)

for i in range(n-1, 0, -1):
    if target[i - 1] < target[i]:
        target = target[:i] + sorted(target[i:])
        for idx, t in enumerate(target):
            if idx < i - 1:
                continue
            if target[i - 1] < t:
                target[i - 1], target[idx] = target[idx], target[i - 1]
                break
        print(*target)
        break
    if i == 1:
        print(-1)
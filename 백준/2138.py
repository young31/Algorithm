from copy import deepcopy
n = int(input())
given = list(map(int, list(input().strip())))
target = list(map(int, list(input().strip())))

def find(given, target):
    cnt = 0
    for i in range(1, n):
        if given[i-1] != target[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                if 0 <= j < n:
                    given[j] = 1 - given[j]
    return given, cnt

answer = float('inf')

res1, cnt1 = find(deepcopy(given), target)
if res1 == target:
    answer = min(answer, cnt1)
tmp = deepcopy(given)
tmp[0] = 1 - tmp[0]
tmp[1] = 1 - tmp[1]
res2, cnt2 = find(tmp, target)
cnt2 += 1
if res2 == target:
    answer = min(answer, cnt2)

if answer == float('inf'):
    print(-1)
else:
    print(answer)

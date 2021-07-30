from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
arr = []
s = 0
cnt = 0
for _ in range(N):
    n = int(input())
    arr.append(n)
    s += n
    cnt += 1

arr.sort()
counter = Counter(arr)
max_ = max(counter.values())
modes = list(filter(lambda x: counter[x] == max_, counter.keys()))
if len(modes) == 1:
    mode = modes[0]
else:
    mode = sorted(modes)[1]
print(round(s/cnt))
print(arr[cnt//2])
print(mode)
print(max(arr) - min(arr))


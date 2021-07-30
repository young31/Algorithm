from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

cnt = Counter(arr)
max_ = max(cnt.values())
print(sorted(list(filter(lambda x: cnt[x] == max_, cnt.keys())))[0])
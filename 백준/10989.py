from collections import defaultdict
import sys
input = sys.stdin.readline

nums = defaultdict(int)
N = int(input())
for _ in range(N):
    nums[int(input())] += 1

keys = sorted(nums.keys())
for k in keys:
    m = nums[k]
    for _ in range(m): print(k)
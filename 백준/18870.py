from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr2 = list(set(arr))
arr2.sort()
ans = defaultdict(int)

ans[arr2[0]]
prev = arr2[0]
for a in arr2[1:]:
    ans[a] = ans[prev]+1
    prev = a

res = list(map(ans.get, arr))
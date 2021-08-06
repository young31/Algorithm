from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

cnt = Counter(arr)

for a in arr2:
    print(cnt[a])

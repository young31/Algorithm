# segment tree
def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start+end)//2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    
    return tree[idx]

def interval_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[idx]
    mid = (start+end)//2
    return interval_sum(start, mid, idx*2, left, right) + interval_sum(mid+1, end, idx*2+1, left, right)

def update(start, end, idx, target, diff):
    if target < start or target > end:
        return
    tree[idx] += diff
    if start == end:
        return
    mid = (start+end)//2
    update(start, mid, idx*2, target, diff)
    update(mid+1, end, idx*2+1, target, diff)

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0 for _ in range(n*4)]
init(0, n-1, 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        c_ = c-arr[b-1]
        arr[b-1] = c
        update(0, n-1, 1, b-1, c_)
    else:
        print(interval_sum(0, n-1, 1, b-1, c-1))
    
# 펜윅 트리
def update(i, d):
    while i <= n:
        tree[i] += d
        i += (i & -i)

def tree_sum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

def interval_sum(a, b):
    return tree_sum(b) - tree_sum(a-1)

n, m, k = map(int, input().split())
tree = [0 for _ in range(n+1)]
arr = [0 for _ in range(n)]
for i in range(n):
    num = int(input())
    update(i+1, num)
    arr[i] = num

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        c_ = c-arr[b-1]
        arr[b-1] = c
        update(b, c_)
    else:
        print(interval_sum(b, c))
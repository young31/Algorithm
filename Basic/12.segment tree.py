# 구간합을 빠르게 구하기 위한 방법
## class로 구현하면 더 이쁠 듯
## 백준 2042
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

def update(start, end, idx, target, value):
    if target < start or target > end:
        return

    tree[idx] = value
    if start == end:
        return
    mid = (start+end)//2
    update(start, mid, idx*2, target, value)
    update(mid+1, end, idx*2+1, target, value)

arr = list(range(10))

n = len(arr)
tree = [0 for _ in range(4*n)] # 4 를 곱하는 것은 적절히 커버할 수 있는 범위(2의 제곱수 따라가기)

init(0, n-1, 1)
print(tree)
print(interval_sum(0, n-1, 1, 0, 10))

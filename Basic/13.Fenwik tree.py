# 누적합을 이용하는 효울적인 자료구조
## 비트 연산을 이용하여 효율적으로 처리
## seg tree 대비 메모리 사용량을 줄일 수 있다.
## 구현도 간단! 

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

arr = list(range(10))
n = len(arr)
tree = [0 for _ in range(n+1)]
for i, a in enumerate(arr, 1):
    update(i, a)
print(tree)
print(tree_sum(4))
print(tree_sum(5))
print(tree_sum(6))
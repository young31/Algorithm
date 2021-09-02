import sys
input = sys.stdin.readline

def update(i, d, arr):
    while i <= 200001:
        arr[i] += d % 1000000007
        i += (i & -i)

def tree_sum(i, arr):
    res = 0
    while i > 0:
        res += arr[i] % 1000000007
        i -= (i & -i)
    return res

def interval_sum(a, b, arr):
    return tree_sum(b, arr) - tree_sum(a-1, arr)

n = int(input())
tree = [0 for _ in range(200002)]
arr = [0 for _ in range(200002)]

k = int(input())+1
update(k, k-1, tree)
update(k, 1, arr)

ans = 1

for _ in range(n-1):
    loc = int(input())+1
    cnt_left = tree_sum(loc, arr)
    amt_left = tree_sum(loc, tree)

    cnt_right = interval_sum(loc+1, 200001, arr)
    amt_right = interval_sum(loc+1, 200001, tree)
    
    s = cnt_left*(loc-1) - amt_left + amt_right - cnt_right*(loc-1)
    ans = (ans*s)%1000000007

    update(loc, 1, arr)
    update(loc, loc-1, tree)

print(ans%1000000007)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

def get(coins, k=k):
    cnt = 0
    for c in reversed(coins):
        ct = k//c
        cnt += ct
        k -= ct*c

    return cnt

ans = float('inf')
for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    coins.append(coin)
    ans = min(ans, get(coins))

print(ans)
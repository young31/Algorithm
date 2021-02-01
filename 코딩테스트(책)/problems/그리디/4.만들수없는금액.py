# input
n1 = 5
coins1 = [3, 2, 1, 1, 9]
n2 = 3
coins2 = [3,5,7]

# answer: 8, 1

# algo
## DP로 작성해 봄
## 1부터 순서대로 들어간 코인 수를 보면서 만들 수 있으면 그 구성을 적어가면서 증가시킴
## 최소 갯수가 아니므로 중간에 최소 갯수로 만드는 과정은 필요 없이 넘어감
def is_feasilbe(x, coins):
    for k in x.keys():
        if x[k] > coins[k]:
            return False
    return True

def gen_dct(dct):
    res = {}
    for k in dct.keys():
        res[k] = 0
    return res

def main(coins):
    # 코인을 딕셔너리로 초기화
    coins = sorted(coins)
    dct = {}
    for c in coins:
        if c in dct.keys():
            dct[c] += 1
        else:
            dct[c] = 1

    coins = dct
    
    ans = [0 for _ in range(int(1e5))]

    # 가지고 있는 코인은 모두 만들 수 있음으로 초기화
    ## 꼭 필요하지는 않을 듯
    for c in coins.keys():
        ans[c] = gen_dct(dct)
        ans[c][c] = 1

    for i in range(1, len(ans)):
        # 코인이 큰 수 부터라면 빠르게 return
        if i < min(coins.keys()):
            return i

        if ans[i] == 0:
            for c in reversed(list(coins.keys())): # 큰 수 부터 채워가야 못 채우는 수가 없음
                if i-c > 0:
                    tmp = ans[i-c].copy()
                    tmp[c] += 1
                    if is_feasilbe(tmp, coins):
                        ans[i] = tmp
                        break
            else: # feasible한 조합이 없다면
                return i

print(main(coins1))
print(main(coins2))
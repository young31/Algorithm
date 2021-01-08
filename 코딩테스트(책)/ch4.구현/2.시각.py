# input
n = 5
# answer: 11475

# algo
def main():
    ans = 0
    for i in range(n+1):
        if i % 10 == 3: # 시간에 들어가면 분초 모두
            ans += 3600
        else:
            ans += (15*60 + 15*60 - 225) # 아닌경우 
    print(ans)
    return ans

main()


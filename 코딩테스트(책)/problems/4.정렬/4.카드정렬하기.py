# input
n = 3
cards = [10, 20, 40]
# answer: 100

# algo
def solution(n, cards):
    cards = sorted(cards)
    mul = reversed(range(1, n+1))

    res = -cards[0]
    for c, m in zip(cards, mul):
        res += c*m
    
    print(res)

solution(n, cards)

# input
n = 3
cards = [10, 20, 40]
# answer: 100

# algo
import heapq
def solution(n, cards):
    card = []
    for c in cards:
        heapq.heappush(card, c)
    
    res = 0
    while len(card) >= 2:
        a = heapq.heappop(card)
        b = heapq.heappop(card)
        res += (a+b)
        heapq.heappush(card, (a+b))

    print(res)

solution(n, cards)

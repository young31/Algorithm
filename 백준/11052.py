n = int(input())
cards = list(map(int, input().split( )))
cards = {i: x for i, x in enumerate(cards, 1)}
slot = [0 for _ in range(n)]

for i in range(n):
    tmp = []
    if i+1 in cards.keys():
        tmp.append(cards[i+1])
    for j, v in cards.items():
        if i-j >= 0:
            tmp.append(slot[i-j]+cards[j])
        else:
            break
    slot[i] = max(tmp)

print(slot[-1])



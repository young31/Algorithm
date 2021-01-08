# input
n, target = 4, 6
stock = [19,15,10,17]

# answer: 15

# algo
def calc_target(point):
    ans = 0
    for s in stock:
        if s > point:
            ans += s-point

    return ans

def search(start, end):
    if start > end:
        return start

    mid = (start + end)//2
    c = calc_target(mid)

    if c == target:
        return mid
    
    elif c < target:
        return search(start, mid-1)

    else:
        if calc_target(mid+1) < target:
            return mid
        else:
            return search(mid+1, end)

def main():
    global stock
    stock = sorted(stock)
    return search(stock[0], stock[-1])

print(main())

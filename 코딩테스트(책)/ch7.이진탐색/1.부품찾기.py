# input
n, m = 5, 3
stock = [8, 3, 7, 9, 2]
req = [5, 7, 9]
# answer: no yes yes

# algo
def search(stock, target, start, end):
    # 정렬먼저하기
    if start > end:
        return 'no'

    mid = (start + end) // 2

    if stock[mid] == target:
        return 'yes'

    elif stock[mid] < target:
        return search(stock, target, mid+1, end)

    elif stock[mid] > target:
        return search(stock, target, start, mid-1)

def main():
    global stock
    stock = sorted(stock)
    for i in req:
        print(search(stock, i, 0, n), end=' ')

main()
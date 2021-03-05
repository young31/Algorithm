# input
n1 = 7
work1 = [
    (3, 10), (5, 20), (1, 10), (1, 20), (2, 15), (4, 40), (2, 200)
]

n2 = 10
work2 = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10)
]

n3 = 10
work3 = [
    (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6)
]

n4 = 10
work4 = [
    (5, 50), (4, 40), (3, 30), (2, 20), (1, 10), (1, 10), (2, 20), (3, 30), (4, 40), (5, 50)
]

# answer: 45, 55, 20, 90

# algo
def solution(n, table):
    ans = [0 for _ in range(n)]

    for i, (d, p) in enumerate(table):
        if i+d-1 < n:
            cum = max(ans[:i]+[0])
            ans[i+d-1] = max(
                ans[i+d-1], cum+p
            )

    print(max(ans))

solution(n1, work1)
solution(n2, work2)
solution(n3, work3)
solution(n4, work4)
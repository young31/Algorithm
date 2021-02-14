# input
n1, m1, k1, x1 = 4, 4, 2, 1
input1 = [
    (1, 2), (1, 3), (2, 3), (2, 4)
]

n2, m2, k2, x2 = 4, 3, 2, 1
input2 = [
    (1, 2), (1, 3), (1, 4)
]

n3, m3, k3, x3 = 4, 4, 1, 1
input3 = [
    (1, 2), (1, 3), (2, 3), (2, 4)
]
# answer: 4/ -1/ 2, 3

# algo
## 단순한 bfs 문제
def main(arr, n, k, x):
    dct = {}
    visited = [False for _ in range(n+1)]
    for i, j in arr:
        if i in dct.keys():
            dct[i].append(j)
        else:
            dct[i] = [j]

    cur = [x]
    epoch = 0

    while 1:
        nxt = []

        for n in cur:
            if n in dct.keys():
                for i in dct[n]:
                    if not visited[i]:
                        nxt.append(i)
                        visited[i] = True

        if len(nxt) == 0:
            return -1

        epoch += 1

        if epoch == k:
            return sorted(nxt)
        cur = nxt

print(main(input1, n1, k1, x1))
print(main(input2, n2, k2, x2))
print(main(input3, n3, k3, x3))
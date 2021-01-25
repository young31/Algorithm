# input
n, m = 7, 12
inputs = [
    (1, 2, 3), (1, 3, 2), (3, 2, 1), (2, 5, 2), (3, 4, 4), (7, 3, 6),
    (5, 1, 5), (1, 6, 2), (6, 4 ,1), (6, 5, 3), (4, 5, 3), (6, 7, 4)
]
# answer: 8

# algo
## 아이디어를 떠올리지 못했다. 신장트리에 대해서 익숙해지자.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main():
    from queue import PriorityQueue
    # initialize 
    parents = [i for i in range(n+1)]
    cost = []

    edges = PriorityQueue()
    for a, b, c in inputs:
        edges.put((c, a, b))

    while edges.qsize() != 0:
        c, a, b = edges.get()
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            cost.append(c)

    # 이 부분이 핵심 아이디어: 최소신장트리 만들고 최대 값을 자르면 된다!
    print(sum(cost) - max(cost))

main()
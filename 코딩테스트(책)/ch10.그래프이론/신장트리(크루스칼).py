# input
v, e = 7, 9
graph = [
    (1, 2, 29), (1, 5, 75), (2, 3, 35), (2, 6, 34), (3, 4, 7), (4, 6, 23), (4, 7, 13), (5, 6, 53), (6, 7, 25)
]
# answer: 159

# algo
## 간선을 거리순으로 정렬한다.
## 만약 해당 간선을 더했을 때 사이클이 생기지 않으면 연결에 포함시킨다.
## 서로조집합의 사이클개념이 여기서 사용된다.

def find_parent(parent, x):
    if parent[x] != x: # 자신이 부모가 아니라면 연결된 부모를 찾는다
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    # 두 노드가 있을 때 숫자가 낮은 값에 할당
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def main():
    from queue import PriorityQueue
    # initialize 
    parents = [i for i in range(v+1)]
    cost = 0

    # 우선순위 안쓰고 그냥 리스트로 정렬해서 사용해도 됨
    edges = PriorityQueue()
    for a, b, c in graph:
        edges.put((c, a, b))

    while edges.qsize() != 0:
        c, a, b = edges.get()
        if find_parent(parents, a) != find_parent(parents, b):
            union_parent(parents, a, b)
            cost += c

    print(cost)

main()

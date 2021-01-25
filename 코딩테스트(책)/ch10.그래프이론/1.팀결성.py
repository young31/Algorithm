# input
n, m = 7, 8
inputs = [
    (0, 1, 3), (1, 1, 7), (0, 7, 6), (1, 7, 1), (0, 3, 7), (0, 4, 2), (0, 1, 1), (1, 1, 1)
]
# answer: NO, NO, YES

# algo
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
    parents = [i for i in range(n+1)]

    for c, a, b in inputs:
        if c == 0:
            union_parent(parents, a, b)
        else:
            if find_parent(parents, a) == find_parent(parents, b):
                print('YES')
            else:
                print('NO')

main()
# input
input_ = [
    (1, 4), (2, 3), (2, 4), (5, 6)
]
n, v = 4, 6
# answer: 1, 1, 1, 1, 5, 5

# algo
# 테이블로 데이터를 가지고 있음
# 그래프 구조를 활용하여 부모 노드를 작성하여 서로소 상태를 확인하는 방법
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
    parent = [i for i in range(v+1)]
    for a, b in input_:
        union_parent(parent, a, b)

    for i in range(1, v+1):
        print(find_parent(parent, i))


def main1():
    # 푸는 법을 몰랐다면 이렇게 짰겠지!
    ## 초기화
    a, b = input_[0]
    SETS = [set((a, b))]
    ## 1차로 집합을 만듬
    for a, b in input_[1:]:
        for s in SETS:
            if a in s or b in s:
                s.add(a)
                s.add(b)
                break
        else:
            SETS.append(set((a, b)))
    ## union되는 부분이 있다면 합쳐주기
    while 1:
        s = SETS[0]
        for i, s_ in enumerate(SETS[1:]):
            if len(s & s_) >= 1:
                SETS[0] = s | s_
                SETS.pop(i+1)
        else:
            break
    print(SETS)

def main2():
    # 사이클 여부를 확인하는 방법
    parent = [i for i in range(v+1)]
    CYCLE = False
    for a, b in input_: # 두 노드의 부모가 같으면 사이클
        if find_parent(parent, a) == find_parent(parent, b):
            CYCLE = True
            break
        else: # 아니면 집합 구분하고 다음으로
            union_parent(parent, a, b)

main1()


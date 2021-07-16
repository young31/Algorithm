def perm(a):
    # 순서대로 추가할 숫자의 순서만 변경하면서 generate
    if len(a) == 1:
        yield a
    
    else:
        for i in range(len(a)):
            for nxt in perm(a[:i] + a[i+1:]):
                if 5 not in nxt: # 여기서 포함되는 조건에 대해서 수행한다.
                    yield [a[i]] + nxt

def perm2(a, cnt, k):
    from copy import deepcopy
    # return의 형태가 아니므로 함수내에서 처리를 하고 global 등의 방식으로 함수 밖으로 건내주어야 한다.
    # 리스트의 경우 카피를 하지 않으면 참조 메모리가 같아서 모두 동일해진다.
    global arr
    if cnt == k:
        arr.append(deepcopy(a[:k]))
        return
        
    for i in range(cnt, len(a)):
        a[i], a[cnt] = a[cnt], a[i]
        if sum(a[:2]) <= 3: # 조건 충족시에만 진행
            perm2(a, cnt+1, k)
            a[i], a[cnt] = a[cnt], a[i]

a = [1, 2, 3, 4, 5]
arr = []

cnt = 0
for i in perm(a):
    cnt += 1

# print(cnt)

# perm2(a, 0, 5)
# print(arr)

arr = []
perm2(a, 0, 5)
print(arr)



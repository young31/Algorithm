# input
n1 = 2
a1 = [5, 6]
op1 = [0, 0, 1, 0]

n2 = 3
a2 = [3, 4, 5]
op2 = [1, 0, 1, 0]

n3 = 6
a3 = [1, 2, 3, 4, 5, 6]
op3 = [2, 1, 1, 1]
# answer: 30, 30 // 35, 17 // 54, -24

# algo
def perm(arr, n, k=0):
    global max_n, min_n, cnt
    cnt += 1
    # print(arr)
    if k == len(arr):
        print(arr)
        res = do_op(n, arr)
        if res > max_n:
            max_n = res
        if res < min_n:
            min_n = res
        return
    else:
        for i in range(k, len(arr)):
            if arr[i] != arr[k]:
                arr[i], arr[k] = arr[k], arr[i]
                perm(arr, n, k+1)
                arr[i], arr[k] = arr[k], arr[i]
            else:
                perm(arr, n, k+1)

def perm(arr):
    global cnt
    # 해당 방식으로는 중복처리를 어떻게 잘라낼지 모르겠다.
    if len(arr) == 1:
        cnt += 1
        yield arr
    else:
        for i in range(len(arr)):
            for nxt in perm(arr[:i] + arr[i+1:]):
                yield [arr[i]] + nxt

def do_op(n, op):
    res = n[0]
    for i, o in enumerate(op, 1):
        if o == 0: # +
            res += n[i]
        elif o == 1: # -
            res -= n[i]
        elif o == 2: # x
            res *= n[i]
        else: # /
            if res >= 0:
                res = res // n[i]
            else:
                tmp = abs(res)
                tmp = tmp // n[i]
                res = -tmp
    return res
        

def main(n, op):
    ops = []
    for i, o in enumerate(op):
        ops += [i for _ in range(o)]
    
    max_n = -float('inf')
    min_n = float('inf')

    for o in perm(ops):
        res = do_op(n, o)
        if res > max_n:
            max_n = res
        if res < min_n:
            min_n = res
    
    print(max_n, min_n)

cnt = 0
main(a1, op1)
print(cnt)
cnt = 0
main(a2, op2)
print(cnt)
cnt = 0
main(a3, op3)
print(cnt)


a = a3
op = op3
ops = []
for i, o in enumerate(op):
    ops += [i for _ in range(o)]

max_n = -float('inf')
min_n = float('inf')
cnt = 0
perm(ops, a)
print(max_n, min_n)
print(cnt)
# solution 1
from itertools import permutations
def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a <= b:
        parents[b] = a 
    else:
        parents[a] = b

def do_op(a, b, op):
    if op == '-':
        return a-b
    elif op == '+':
        return a+b
    elif op == '*':
        return a*b

def solution(expression):
    op_type = ['-', '+', '*']
    # parsing
    nums = []
    ops = []
    k = ''
    for exp in expression:
        if exp not in op_type:
            k += exp
        else:
            nums.append(int(k))
            ops.append(exp)
            k = ''
    nums.append(int(k))

    # main
    answer = 0
    for op_seq in permutations(op_type):
        parents = list(range(len(nums)))
        parents_value = {i: x for i, x in enumerate(nums)}

        for op_s in op_seq:
            for i, op in enumerate(ops):
                if op == op_s:
                    p_a = find(parents, i)
                    p_b = find(parents, i+1)
                    op_result = do_op(parents_value[p_a], parents_value[p_b], op)
                    parents_value[p_a] = op_result
                    parents_value[p_b] = op_result
                    union(parents, i, i+1)
                    

        answer = max(answer, abs(parents_value[0]))
    return answer

# solution 2
def parse(x):
    ops = []
    for i in x:
        if i in ['+', '-', '*']:
            ops.append(i)
    for op in ['+', '-', '*']:
        x = x.replace(op, '_')
    numbers = x.split('_')
    
    return numbers, ops

def operation(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

def solution(expression):
    from itertools import permutations
    from copy import deepcopy

    numbers, ops = parse(expression)
    numbers = list(map(int, numbers))

    uops = set(ops)

    answer = 0
    for op in permutations(uops):
        tmp = 0
        tnum = deepcopy(numbers)
        tops = deepcopy(ops)
        for o in op:
            while 1:
                if o not in tops:
                    break

                idx = tops.index(o)
                tops.pop(idx)
                a, b = tnum[idx], tnum[idx+1]                
                tnum = tnum[:idx] + [operation(a, b, o)] + tnum[idx+2:]
        
        answer = max(answer, abs(tnum[0]))

    return answer
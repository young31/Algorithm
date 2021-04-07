# input
expression = "50*6-3*2"

# answer: 300

# algo
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
    print(answer)
    return answer

solution(expression)
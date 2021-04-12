operations = ["I 7","I 5","I -5","D -1", "D -1", "D -1", "D -1"]

import heapq

def solution(operations):
    answer = [0, 0]
    arr = []
    for op in operations:
        if op[0] == 'I':
            _, n = op.split(' ')
            n = int(n)
            heapq.heappush(arr, n)
        elif arr:
            if int(op.split(' ')[1]) == -1:
                arr.pop(0)
            else:
                arr.pop()
    if arr:
        answer = [max(arr), min(arr)]
    return answer

solution(operations)
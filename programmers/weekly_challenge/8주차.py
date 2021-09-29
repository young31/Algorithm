def solution(sizes):
    answer = 0
    sizes = list(map(sorted, sizes))
    a = max([x[0] for x in sizes])
    b = max([x[1] for x in sizes])
    answer = (a*b)
    return answer

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))
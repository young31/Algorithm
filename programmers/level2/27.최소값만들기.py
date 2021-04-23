A = [1,4,2]
B = [5,4,4]


def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    B = reversed(B)

    for a, b in zip(A, B):
        answer += a*b
    print(answer)
    return answer

solution(A, B)
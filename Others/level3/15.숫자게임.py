A = [5,1,3,7]
B = [2,2,6,8]
A = [2,2,2,2]
B = [1,1,1,1]



def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    l = r = 0
    n = len(B)

    while r < n:
        if A[l] < B[r]:
            l += 1
            r += 1
            answer += 1
        else:
            r += 1
    print(answer) 
    return answer

solution(A, B)
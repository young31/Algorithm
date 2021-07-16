arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

def solution(arr1, arr2):
    answer = [[]]
    n = len(arr1)
    m = len(arr2[0])
    k = len(arr1[0])

    answer = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for t in range(k):
                answer[i][j] += arr1[i][t]*arr2[t][j]
    print(answer)
    return answer

solution(arr1, arr2)
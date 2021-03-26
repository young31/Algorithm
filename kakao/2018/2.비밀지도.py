# input
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

# answer: ["#####","# # #", "### #", "# ##", "#####"]

# algo
def solution(n, arr1, arr2):
    def binary_fill(x, n=n):
        res = [0] * n
        for i in range(n):
            power = n-i-1
            if x // (2**power) == 1:
                res[i] = 1
                x = x - (2**power)
        return res

    arr1 = list(map(binary_fill, arr1))
    arr2 = list(map(binary_fill, arr2))

    answer = []
    for i in range(n):
        tmp = ''
        for a1, a2 in zip(arr1[i], arr2[i]):
            if a1+a2 >= 1:
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer

print(solution(n, arr1, arr2))
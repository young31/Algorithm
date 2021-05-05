array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []

    for i, j, k in commands:
        arr = sorted(array[i-1:j])
        print(arr)
        answer.append(arr[k-1])
    
    print(answer)
    return answer

solution(array, commands)
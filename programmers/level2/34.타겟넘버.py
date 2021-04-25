numbers = [1,1,1,1,1]
target = 3


def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def search(i, numbers, mid):
        nonlocal answer
        if i == n:
            if mid == target:
                answer += 1
            return
        
        search(i+1, numbers, mid+numbers[i])
        search(i+1, numbers, mid-numbers[i])
        

    search(0, numbers, 0)

    print(answer)
    return answer


solution(numbers, target)
numbers = [2,1,3,4,1] 

def solution(numbers):
    answer = set()
    numbers.sort()
    n = len(numbers)

    for i in range(n-1):
        for j in range(i+1, n):
            a = numbers[i]+numbers[j]
            answer.add(a)

    answer = list(answer)                  
    print(answer)
    return sorted(answer)
    
solution(numbers)
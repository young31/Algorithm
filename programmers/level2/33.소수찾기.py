numbers="011"

from itertools import permutations

def is_prime(n):
    if n in [0, 1]:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    used = []
    n = len(numbers)

    for i in range(1, n+1):
        for c in permutations(numbers, i):
            num = ''.join(c)
            num = int(num)
            print(num)
            if num not in used and is_prime(num):
                answer += 1
                used.append(num)
    print(used)
    print(answer)
    return answer

solution(numbers)
nums = [1,2,3,4]

from itertools import combinations

def is_prime(x):
    m = int(x**0.5)+1
    for i in range(2, m):
        if x%i==0:
            return False
    return True

def solution(nums):
    answer = 0

    for com in combinations(nums, 3):
        k = sum(com)
        if is_prime(k):
            answer += 1
    return answer

solution(nums)
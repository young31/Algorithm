# input
n1 = 10
n2 = 4

# answer: 12, 4

# algo
def solution(n):
    nums = [1, 2, 3, 4, 5]
    if len(nums) > n:
        return nums[n-1]

    i = 6
    while 1:
        for j in [2, 3, 5]:
            if i % j == 0:
                nums.append(i)
                break
        i += 1
        if len(nums) >= n:
            return nums[n-1]

print(solution(n1))
print(solution(n2))
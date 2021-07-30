from itertools import permutations, product

n = int(input())

numbers = [
    list(input()) for _ in range(n)
]

char = set()
for nums in numbers:
    for num in nums:
        char.add(num)

def convert(nums):
    new_nums = list(map(lambda x: dct.get(x), nums))
    res = ''.join(new_nums)
    return res

ans = 0
for perm in permutations(range(10), len(char)):
    dct = {}
    for c, p in zip(char, perm):
        dct[c] = str(p)
    tmp = list(map(lambda x: int(convert(x)), numbers))
    ans = max(sum(tmp), ans)

print(ans)
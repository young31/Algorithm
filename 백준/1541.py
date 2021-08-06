def parsing(s):
    nums = []
    ops = []
    if s[0] != '-':
        ops.append('+')
    tmp = ''
    for i in s:
        if i in ['+', '-']:
            ops.append(i)
            if tmp != '':
                nums.append(int(tmp))
                tmp = ''
        else:
            tmp += i
    if tmp != '':
        nums.append(int(tmp))
    return nums, ops

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

s = input()

nums, ops = parsing(s)
parents = list(range(len(nums)))

for i, op in enumerate(ops):
    if op == '-':
        di = 1
        while i+di < len(nums):
            if ops[i+di] == '-':
                break
            else:
                nums[i] += nums[i+di]
                union(parents, i, i+di)

            di += 1

used = [False for _ in range(len(nums))]
ans = 0
for i, (n, o) in enumerate(zip(nums, ops)):
    if not used[find(parents, i)]:
        if o == '+':
            ans += n
        else:
            ans -= n
        used[find(parents, i)] = True
print(ans)

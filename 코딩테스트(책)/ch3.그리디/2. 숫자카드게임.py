# # case 1
# n = 3; m = 3
# arr = [
#     [3, 1, 2],
#     [4, 1, 4],
#     [2, 2, 2]
# ]
# case 2
n = 2; m = 4
arr = [
    [7, 3, 1, 8],
    [3, 3, 3, 4]
]

ans = 0

for i in range(len(arr)):
    tmp = min(arr[i])
    if ans <= tmp:
        ans = tmp
print(ans)
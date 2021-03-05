# input
n = 7
arr = [15, 11, 4, 8, 5, 2, 4]

# answer: 2

# algo
length = [1] * n
for i in range(n): # starting point
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            length[j] = max(length[i]+1, length[j])     

print(n - max(length))
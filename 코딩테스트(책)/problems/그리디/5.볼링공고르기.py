# input
n1, m1 = 5, 3
arr1 = [1, 3, 2, 3, 2]

n2, m2 = 8, 5
arr2 = [1, 5, 4, 3, 2, 4, 5, 2]
# answer: 8, 25

# algo
def main(arr):
    arr = sorted(arr)
    cnt = 0
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] != arr[j]:
                cnt += 1
                
    print(cnt)

main(arr1)
main(arr2)
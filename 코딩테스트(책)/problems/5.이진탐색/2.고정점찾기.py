# input
n1 = 5; arr1 = [-15, -6, 1, 3, 7] 
n2 = 7; arr2 = [-15, -4, 2, 8, 9, 13, 15]
n3 = 7; arr3 = [-15, -4, 3, 8, 9, 13, 15]
# answer: 3. 2, -1

# algo
# 고정점이 다수 있을 수 있다는 문구가 없으므로 하나라고 가정하고 풀이(고정점이 있다면)
def find(arr, start, end):
    if start > end:
        return -1

    mid = (start+end)//2
    if arr[mid] == mid:
        return mid

    if arr[mid] < mid:
        return find(arr, mid+1, end)
    
    elif arr[mid] > mid:
        return find(arr, 0, mid-1)


def main(arr):
    res = find(arr, 0, len(arr))
    print(res)

main(arr1)
main(arr2)
main(arr3)
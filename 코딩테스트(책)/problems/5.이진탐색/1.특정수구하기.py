# input
n1,  x1 = 4, 2
arr1 = [1, 1, 2, 2, 2, 2, 3]

n2, x2 = 7, 4
arr2 = [1, 1, 2, 2, 2, 2, 3]
# answer: 4, -1

# algo
# 기본 파이썬 리스트 함수로 count를 쓰면 시간복잡도가 얼마인지 고려해봐야겠다.
def find_left(arr, x, mid):
    # mid = len(arr)//2
    if arr[mid] == x and arr[mid-1] != x:
        return mid
    elif arr[mid] < x:
        return find_left(arr, x, mid + (len(arr[mid+1:])+1)//2)
    else:
        return find_left(arr, x, mid - (len(arr[:mid-1])+1)//2)

def find_right(arr, x, mid):
    if arr[mid] == x and arr[mid+1] != x:
        return mid
    elif arr[mid] <= x:
        return find_right(arr, x, mid + (len(arr[mid+1:])+1)//2)
    else:
        return find_right(arr, x, mid - (len(arr[:mid-1])+1)//2)

def main(arr, x):
    if x not in arr:
        print(-1)
        return 
    left = find_left(arr, x, len(arr)//2)
    right = find_right(arr, x, len(arr)//2)
    print(right - left+1)

main(arr1, x1)
main(arr2, x2)
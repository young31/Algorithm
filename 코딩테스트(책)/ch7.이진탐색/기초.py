array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7

def binary_search(array, target, start, end):
    '''정렬된 경우에만 사용할 수 있음'''
    if start > end:
        return

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
        
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)

    
print(binary_search(array, target, 0, len(array)))
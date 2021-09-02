arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

def quickSort(s, e, c=0):
    global arr
    if s >= e:
        return

    i = s+1
    j = e
    # key = s
    while i <= j:
        while i <= e and arr[i] <= arr[s]: # key 보다 큰 숫자 위치 찾기
            i += 1

        while j > s and arr[j] >= arr[s]: # key 보다 작은 위치 찾기
            j -= 1

        if i > j:
            arr[j], arr[s] = arr[s], arr[j] # 엇갈렸으면 위치가 역전 => 교체
        else:   
            arr[i], arr[j] = arr[j], arr[i] # 아니면 i, j를 교체

    quickSort(s, j-1, c+1)
    quickSort(j+1, e, c+1)
    
quickSort(0, len(arr)-1)
def heapify(arr, idx, n):
    # tree 의 노드 위치
    l = idx*2
    r = idx*2+1
    s = idx
    # 부모가 작은 값을 가지고 나머지도 좌우에 맞게 배열
    if l <= n and arr[s] < arr[l]: # 부등호 방향 -> 최대 힙 / 최소 힙 결정
        s = l
    if r <= n and arr[s] < arr[r]:
        s = r
    if s != idx:
        arr[idx], arr[s] = arr[s], arr[idx]
        return heapify(arr, s, n)


def heapSort(arr):
    n = len(arr)
    arr = [0] + arr # indexing 을 위한 패딩

    for i in range(n, 0, -1):
        heapify(arr, i, n)

    for i in range(n, 0, -1):
        arr[i], arr[1] = arr[1], arr[i]
        heapify(arr, 1, i-1)
    print(arr)
    return arr[1:]


def heapify(arr, idx, n):
    l = idx*2+1
    r = idx*2+2
    s = idx
    if l < n and arr[s] < arr[l]:
        s = l
    if r < n and arr[s] < arr[r]:
        s = r
    if s != idx:
        arr[idx], arr[s] = arr[s], arr[idx]
        heapify(arr, s, n)


def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
        
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    print(arr)
    return arr

arr = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]

heapSort(arr)


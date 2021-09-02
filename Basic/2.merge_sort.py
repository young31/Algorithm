def merge(l, r):
    # 두 리스트를 받아서 작은 수 부터 차례대로 merge
    res = []
    i_l = 0
    i_r = 0
    while len(l) > i_l or len(r) > i_r:
        if len(l) > i_l and len(r) > i_r:
            if l[i_l] <= r[i_r]:
                res.append(l[i_l])
                i_l += 1
            else:
                res.append(r[i_r])
                i_r += 1
        elif len(l) > i_l:
            res.append(l[i_l])
            i_l += 1
        elif len(r) > i_r:
            res.append(r[i_r])
            i_r += 1
    return res

def mergeSort(arr):
    # 원소가 하나까지 쪼개고
    if len(arr) <= 1:
        return arr

    # 합치면서 정렬
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]
    l = mergeSort(l)
    r = mergeSort(r)
    return merge(l, r)

arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

print(mergeSort(arr))
lst = [9,5,4,1,0,2,6,8,7,3]

def selection_sort(ls):
    n = len(ls)
    for i in range(0, n):
        for j in range(i+1, n):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
    return ls


def insertion_sort(ls):
    n = len(ls)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if ls[j] < ls[j-1]:
                ls[j], ls[j-1] = ls[j-1], ls[j]
            else:
                break
    return ls


def quick_sort(ls):
    if len(ls) <= 1:
        return ls

    pivot = ls[0]
    tail = ls[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


print(selection_sort(lst))
print(insertion_sort(lst))
print(quick_sort(lst))
n = int(input())

def check(x):
    k = str(x)
    if '666' in k:
        return True
    return False


arr = [x for x in range(666, 2666801) if check(x)]

print(arr[n-1])
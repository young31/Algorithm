import sys
input = sys.stdin.readline

arr = list(map(int, list(input().strip())))
arr = list(map(str, sorted(arr, reverse=True)))
print(''.join(arr))

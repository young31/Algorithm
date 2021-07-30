import sys
input = sys.stdin.readline

N = int(input())
arr = []
names = []
for i in range(N):
    age, name = input().split()
    arr.append((int(age), i))
    names.append(name)

arr.sort()

for a, i in arr:
    print(a, end=' ')
    print(names[i])


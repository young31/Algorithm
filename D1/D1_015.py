# young 130ms, 99
N = int(input())
data = list(map(int, input().split()))
data.sort()
n = int((N-1)/2)
print(data[n])
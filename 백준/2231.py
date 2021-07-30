n = list(input())
l = len(n)
n = int(''.join(n))

for i in range(max(0, n-9*l), n):
    k = list(map(int, list(str(i))))
    if sum(k)+i == n:
        print(i)
        break
else:
    print(0)

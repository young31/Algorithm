#116ms, 101
n = int(input())

for i in range(n+1, 0, -1) :
    if i == 0 :
        print(0)
    print(i-1, end=' ')

print(time.time() - start)
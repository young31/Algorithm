# young
T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
for i in range(1, T + 1):
    (a1, a2, a3, a4) = list(map(int, input().split( )))
    dif = -(sum(days[0:a1-1]) + a2) + (sum(days[0:a3-1]) + a4)+1
    print('#%d'%i, dif)
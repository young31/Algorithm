# young
# 7/10; 수학적으로 접근해서 풀었는데 어디서 오답이..
def comb(i, j):
    n = 1
    for k in range(1,j+1):
        n *= (i/k)
        i -= 1
    return int(n)

for i in range(1, int(input())+1):
    n = 0
    j = int(input())/10
    k = 0
    while j - k >= 0:
        n += (comb(j, k) * (2**k))
        j -= 1
        k += 1
    print('#%d'%i, n)
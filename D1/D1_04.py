N = int(input())

k=[]
for i in range(1, N+1) : 
    if N % i == 0 :
        k.append(str(i))
j = " ".join(k)
print(j)

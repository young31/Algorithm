# young
for i in range(1, int(input())+1):
    l1 = input()
    l2 = input()
    print('#%d'%i, end= ' ')
    if l1 in l2:
        print(1)
    else :
        print(0)
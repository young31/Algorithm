# young 135ms, 202
T = input()
 
for i in range(1,4):
    l = list(map(int, input().split()))
    if l[0] < l[1] :
        k = "<"
    elif l[0] == l[1] :
        k = "="
    else : k= ">"
    print("#{0} {1}".format(i,k))
    
    

# jeong 123ms, 219

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='
    
    print(f'#{i + 1} {result}')

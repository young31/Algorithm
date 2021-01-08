# 122ms, 191
[a, b] =list(map(int,input().split( )))

def go_(a,b) :
    if (a==1 and b == 3) or (a==2 and b==1) or (a == 3 and b ==2) :
        print("A")
    else : 
        print("B")
        
go_(a,b)

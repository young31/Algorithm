# young 132ms, 115
def make_num(a):
    return ord(a)-64
 
t = list(input())
for i in range(len(t)):
    print(make_num(t[i]), end=' ')
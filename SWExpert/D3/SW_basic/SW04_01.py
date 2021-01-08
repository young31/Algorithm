# young 126ms, 211
def double(x, y):
    if y <= 1:
        return x
    double(x, y - 1)
    return x * double(x, y - 1)
 
 
for i in range(1, 11):
    input()
    a, b = map(int, input().split())
    print('#%d' % i, double(a, b))
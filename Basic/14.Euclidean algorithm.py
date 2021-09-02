# 최소공배수 / 최대공약수를 구하는 법
## 이제 인수분해 과정없이 구해보자!

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def LCM(a, b):
    return a * b // GCD(a, b)

a = 1071
b = 1029

print(GCD(a, b))
print(LCM(a, b))
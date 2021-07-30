from collections import deque

n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    ans = deque([1, 3], maxlen=2)
    k = 2
    while k != n:
        ans.append(2*ans[0] + ans[1])
        k += 1
    print(ans[-1]%10007)
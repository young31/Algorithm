s = "baby" # 9
# s = 'pp'
# s = "abaacb"
s = "abcabac"
s = "aaannnaaa"

def find(s):
    n = len(s)
    arr = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                arr[j] = max(arr[j-1], arr[j])
            else:
                arr[j] = max(arr[j], j-i)
    return arr

from pprint import pprint

def solution(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    answer = 0

    k = 1
    while k <= n:
        i = 0
        while i+k < n:
            dp[i][i+k] = k if s[i] != s[i+k] else max(dp[i][i+k-1], dp[i+1][i+k])
            answer += dp[i][i+k]
            i += 1
        
        k += 1
    pprint(dp)
    print(answer)
    return answer
solution(s)

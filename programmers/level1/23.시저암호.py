def solution(s, n):
    def convert(k, n=n):
        if k == 32:
            return 32
        
        if 97 <= k <= 122:
            if k+n > 122:
                return 96 + (k+n)%122
            else:
                return k+n
                
        
        if 65 <= k <= 90:
            if k+n > 90:
                return 64 + (k+n)%90 
            else:
                return k+n
                 

    
    answer = ''.join([chr(convert(ord(x), n)) for x in s])
    return answer


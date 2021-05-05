def solution(arr, divisor):
    answer = [x for x in arr if x%divisor==0]
    if not answer:
        answer = [-1]
    else:
        answer = sorted(answer)
    return answer
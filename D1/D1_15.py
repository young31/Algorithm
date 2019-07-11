# young 130ms, 99
N = int(input())
data = list(map(int, input().split()))
data.sort()
n = int((N-1)/2)
print(data[n])



# jeong 120ms, 154
n = int(input())
num_list = list(map(int, input().split()))
sorted_num_list = sorted(num_list)
median_index = n // 2

print(sorted_num_list[median_index])

'''
코드에서 다른 부분은 .sort(), sorted() 함수 차이만 나는데 
저번 .reverse() / reversed()와 마찬가지로 원본을 바꾸는 .sort(), .reverse()가 조금 더 실행 속도가 더디네요.
'''

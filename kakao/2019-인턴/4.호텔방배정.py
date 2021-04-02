# input
k = 10
room_number = [1,3,4,1,3,1]
# answer: [1,3,4,2,5,6]

# algo
# 이진탐색은 실패
# find_parent방식으로 처리해야 해결 가능
import sys
sys.setrecursionlimit(int(2e9+1))
def solution(k, room_number):
    answer = []
    max_ = 0
    occupied = [1 for _ in range(k+1)]
    occupied[0] = 0

    for rn in room_number:
        if occupied[rn] == 1:
            answer.append(rn)
            occupied[rn] = 0
            if rn > max_:
                max_ = rn
        else:
            s = rn+1
            e = max_+1
            while s<=e:
                mid = (s+e)//2
                sum_ = sum(occupied[s:mid])
                if occupied[mid] and sum_==0:
                    occupied[mid] = 0
                    answer.append(mid)
                    if mid > max_:
                        max_ = mid
                    break
                elif sum_ > 0:
                    e = mid-1
                else:
                    s = mid+1
    print(answer)
    return answer

def solution(k, room_number):
    def find_parent(x):
        if x not in parents.keys():
            parents[x] = x+1
            return x

        else:
            parent = find_parent(parents[x])
            parents[x] = parent+1
            return parent

    answer = []
    # parents = [0 for _ in range(k+1)]
    parents = {}

    for rn in room_number:
        answer.append(find_parent(rn))
    print(answer)
    return answer

solution(k, room_number)
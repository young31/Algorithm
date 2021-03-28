# input
food_times = [3, 1, 2]
k = 5
# answer: 

# algo
def solution(food_times, k):
    food_to_eat = []
    for i, f in enumerate(food_times, 1):
        food_to_eat.append([f, i])

    food_to_eat = sorted(food_to_eat)

    total_f = 0
    idx = 0
    while 1:
        n = len(food_to_eat)-idx
        f = food_to_eat[idx][0] - total_f
        if n*f > k:
            ft = food_to_eat[idx:]
            ft = sorted(ft, key=lambda x: x[1])
            return ft[k%n][1]
        else:
            k -= n*f
            total_f += f
            idx += 1
            if len(food_to_eat)-idx <= 0:
                return -1

    
print(solution(food_times, k))

    
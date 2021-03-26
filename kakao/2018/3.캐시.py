# input
n = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

# answer: 52

# algo
from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    else:
        answer = 0
        cities = list(map(lambda x: x.lower(), cities))
        cache = deque([], maxlen=cacheSize)

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.appendleft(city)
            answer += 1
        else:
            cache.appendleft(city)
            answer += 5
    return answer

print(solution(n, cities))
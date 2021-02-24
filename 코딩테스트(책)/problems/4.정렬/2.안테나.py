# input
n = 4
house = [5, 1, 7, 9]
# answer: 5

# algo
house = sorted(house)
mid = house[(n-1)//2]
print(house[house.index(mid)])
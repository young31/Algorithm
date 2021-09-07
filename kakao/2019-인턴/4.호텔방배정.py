# solution 1
from collections import defaultdict
import sys
sys.setrecursionlimit(int(2e9+1))

def find(parent, x):
    if not parent[x]:
        parent[x] = x
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

def solution(k, room_number):
    answer = []
    # parents = {i: i for i in range(1, k+1)}
    parents = defaultdict(bool)
    for n in room_number:
        answer.append(find(parents, n))
        union(parents, n, find(parents, n)+1)
        
    return answer

k = 10
room_number = [1,3,4,1,3,1]

print(solution(k, room_number))

# solution 2
import sys
sys.setrecursionlimit(int(2e9+1))

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
    parents = {}

    for rn in room_number:
        answer.append(find_parent(rn))

    return answer
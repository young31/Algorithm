from collections import defaultdict, Counter
import sys
input = sys.stdin.readline

def false():
    return False

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    s = cnt_dct[a] + cnt_dct[b]

    if a < b:
        parent[b] = a
        cnt_dct[b] = s
        cnt_dct[a] = s
    elif a > b:
        parent[a] = b
        cnt_dct[a] = s
        cnt_dct[b] = s

N = int(input())
for _ in range(N):
    n = int(input())
    parents = defaultdict(false)
    cnt_dct = {}
    num = 0
    for _ in range(n):
        a, b = input().split()
        if not parents[a]:
            parents[a] = a
            cnt_dct[a] = 1
            
        if not parents[b]:
            parents[b] = b
            cnt_dct[b] = 1

        union(parents, a, b)
        print(cnt_dct[find(parents, a)])
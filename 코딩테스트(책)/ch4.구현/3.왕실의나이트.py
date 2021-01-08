# input
cur1 = 'a1' # 2
cur2 = 'c2' # 6

# algo
available_movements = [
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2)
]

def loc(cur):
    x = ord(cur[0])-96
    y = int(cur[1])
    return (x, y)

def is_feasible(cur, move):
    if 0 < cur[0]+move[0] <= 8 and 0< cur[1]+move[1] <= 8:
        return True
    return False

def main():
    for cur in [cur1, cur2]:
        ans = 0
        cur = loc(cur)
        for m in available_movements:
            ans += is_feasible(cur, m)
        print(ans)

main()
    
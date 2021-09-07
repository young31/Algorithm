# solution 1
key_map = {
    1: (0, 0), 2: (1, 0), 3: (2, 0),
    4: (0, 1), 5: (1, 1), 6: (2, 1),
    7: (0, 2), 8: (1, 2), 9: (2, 2),
    '*': (0, 3), 0: (1, 3), '#': (2, 3),
}

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solution(numbers, hand):
    left_group = [1, 4, 7]
    right_group = [3, 6, 9]
    l = '*'; r = '#'
    ans = ''

    hand = 'L' if hand == 'left' else 'R'

    for num in numbers:
        if num in left_group:
            ans += 'L'
            l = num
        elif num in right_group:
            ans += 'R'
            r = num
        else:
            d_l = dist(key_map[l], key_map[num])
            d_r = dist(key_map[r], key_map[num])
            if d_l > d_r:
                ans += 'R'
                r = num
            elif d_l < d_r:
                ans += 'L'
                l = num
            else:
                ans += hand
                if hand == 'L':
                    l = num
                else:
                    r = num
    return ans

# solution 2
table = {
    1: (0, 0), 4: (1, 0), 7: (2, 0), '*': (3, 0),
    3: (0, 2), 6: (1, 2), 9: (2, 2), '#': (3, 2),
    2: (0, 1), 5: (1, 1), 8: (2, 1), 0: (3, 1)
}

def dist(x, y):
    x1, x2 = table[x]
    y1, y2 = table[y]
    d = abs(x1-y1) + abs(x2-y2)
    return d

class Hand:
    def __init__(self, mod):
        self.mod = mod
        self.left = '*'
        self.right = '#'
        self.history = []

    def push(self, key):
        if key in [1, 4, 7]:
            self.left = key
            return 'L'
        elif key in [3, 6, 9]:
            self.right = key
            return 'R'
        else:
            ld = dist(self.left, key)
            rd = dist(self.right, key)

            if self.mod == 'left':
                if ld <= rd:
                    self.left = key
                    return 'L'
                else:
                    self.right = key
                    return 'R'
            else:
                if rd <= ld:
                    self.right = key
                    return 'R'
                else:
                    self.left = key
                    return 'L'

def solution(numbers, hand):
    answer = ''
    controller = Hand(hand)
    for n in numbers:
        res = controller.push(n)
        answer += res

    return answer
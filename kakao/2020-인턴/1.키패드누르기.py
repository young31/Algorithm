# input
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
# answer: 

# algo

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

solution(numbers, hand)
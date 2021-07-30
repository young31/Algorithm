import sys

class Solver:
    def __init__(self):
        self.S = set()

    def do(self, op, x=None):
        if op == 'add':
            self.add(x)
        elif op == 'remove':
            self.remove(x)
        elif op == 'check':
            self.check(x)
        elif op == 'toggle':
            self.toggle(x)
        elif op == 'all':
            self.all()
        elif op == 'empty':
            self.empty()

    def add(self, x):
        self.S.add(x)

    def remove(self, x):
        if x in self.S:
            self.S.remove(x)

    def check(self, x):
        if x in self.S:
            print(1)
        else:
            print(0)

    def toggle(self, x):
        if x in self.S:
            self.S.remove(x)
        else:
            self.S.add(x)

    def all(self):
        self.S = set(range(1, 21))
    
    def empty(self):
        self.S = set()

n = int(input())
solver = Solver()

for _ in range(n):
    q = sys.stdin.readline().strip().split()
    if len(q) == 1:
        solver.do(q[0])
    else:
        solver.do(q[0], int(q[1]))


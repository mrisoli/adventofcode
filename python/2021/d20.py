from utils import fopen
from itertools import product

def it(a):
    return [int(p=='#') for p in a]

g = list(product((-1, 0, 1), repeat=2))
adj = lambda d: {(x + dx, y + dy) for x, y in d for dy, dx in g}

class Image:
    def __init__(self, a, i):
        self.a = [int(p=='#') for p in a]
        self.img = {(x,y): int(p=='#')
                    for x, r in enumerate(i.splitlines())
                    for y, p in enumerate(r)}

    def adj(self):
        return {(x + dx, y + dy) for x, y in self.img for dy, dx in g}

    def cv(self, i, j, d):
        s = [str(self.img.get((i + di,j + dj), d)) for di, dj in g]
        n = int(''.join(s),2)
        return self.a[n]

    def tr(self, c):
        for s in range(c):
            d = self.a[0] if s % 2 else 0
            self.img = {(x,y): self.cv(x, y, d) for x, y in self.adj()}

    def count(self):
        print(sum(self.img.values()))

    def pp(self):
        print('----------')
        print(self.img)

def solve(n):
    img = Image(*fopen(20).read().split('\n\n'))
    img.tr(n)
    img.count()

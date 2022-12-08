from utils import fopen

def yield_points(g):
    for i in range(1, len(g) - 1):
        for j in range(1, len(g) - 1):
            yield(i,j)

def get_grid():
    return [[int(y) for y in x.strip()] for x in fopen(8).readlines()]

def nrange(v):
    return range(v - 1, -1, -1)

def prange(v, g):
    return range(v + 1, len(g))

class Point:
    def __init__(self, g, i, j):
        self.g = g
        self.i = i
        self.j = j

    def check(self, fn):
        return self.checkfn(fn)

    def get(self, i=None,j=None):
        if i is None:
            i = self.i
        if j is None:
            j = self.j
        return self.g[i][j]

    def top(self):
        return self.check(map(lambda ii: self.get(i=ii),  nrange(self.i)))

    def right(self):
        return self.check(map(lambda jj: self.get(j=jj),  prange(self.j, self.g)))

    def bottom(self):
        return self.check(map(lambda ii: self.get(i=ii),  prange(self.i, self.g)))

    def left(self):
        return self.check(map(lambda jj: self.get(j=jj),  nrange(self.j)))

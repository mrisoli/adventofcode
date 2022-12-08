from dataclasses import dataclass
from utils import fopen

class Grid:
    def __init__(self):
        self.g = [[int(y) for y in x.strip()] for x in fopen(8).readlines()]
        self.len = len(self.g)

    def yield_points(self):
        for i in range(1, self.len - 1):
            for j in range(1, self.len - 1):
                yield(i,j)

    def nrange(self, v):
        return range(v - 1, -1, -1)

    def prange(self, v):
        return range(v + 1, self.len)

    def ranges(self):
        return [self.nrange, self.prange]

    def get(self, i, j):
        return self.g[i][j]

@dataclass
class Point:
    g: list[list[int]]
    i: int
    j: int

    def get(self, o=None, v=None):
        return self.g.get(v if o == 'r' else self.i, v if o == 'c' else self.j)

    def directions(self, o, d):
        return map(lambda v: self.get(o, v), d(self.i if o == 'r' else self.j))

    def get_predicates(self):
        return [self.checkfn(self.directions(o, d)) for o in ('r','c') for d in self.g.ranges()]

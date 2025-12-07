from utils import coords
from functools import lru_cache

class Timelines:
    def __init__(self):
        self.grid = coords(7, tokens='S^')
        self.limit = round(max(map(lambda x: x.real, self.grid)))
        self.start = next(k for k, v in self.grid.items() if v == 'S')

    def filter_row(self, f, c):
        points = set()
        for k,v in f.items():
            if k.real == c and v in '|S':
                points.add(k)
        return points

    def run(self):
        f = dict(self.grid)
        for c in range(0, self.limit + 1):
            points = self.filter_row(f, c)
            for p in points:
                if p + 1 in self.grid.keys() and self.grid[p + 1] == '^':
                    f[p + 1 -1j] = '|'
                    f[p + 1 +1j] = '|'
                else:
                    f[p + 1] = '|'
        self.grid = dict(f)

    @lru_cache
    def paths(self, p):
        if p.real > self.limit:
            return 1
        if self.grid[p] == '^':
            return self.paths(p + 1 - 1j) + self.paths(p + 1 + 1j)
        return self.paths(p + 1)

    def solve(self):
        self.run()
        print(self.paths(self.start))

Timelines().solve()

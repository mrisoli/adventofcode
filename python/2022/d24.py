from utils import str_list

class Blizzard:
    def __init__(self,):
        l = str_list(24)
        self.h = len(l) - 2
        self.w = len(l[0]) - 2
        self.b = f = self.make(l)

    def wrap(self, p):
        return complex(p.real % self.h, p.imag % self.w)

    def make(self, l):
        d = {'^': -1, 'v': 1, '<': -1j, '>': 1j, 'x': 0}
        return {d[k]: {complex(x,y) for x in range(self.h) for y in range(self.w) if l[x+1][y+1] == k} for k in d}

    def rotate(self):
        self.b = {k: {self.wrap(p + k) for p in v} for k,v in self.b.items()}

    def points(self):
        return {v for ps in self.b.values() for v in ps}

    def dirs(self):
        return self.b.keys()

def run(b, s, g):
    q, i = [s], 0
    while q:
        b.rotate()
        i += 1
        c = {p + m for p in q for m in b.dirs()}
        if g in c:
            return i
        q = []
        c = c - b.points()
        c = filter(lambda p: p == b.wrap(p) or p in (s,g), c)
        q = list(c)

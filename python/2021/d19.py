from math import hypot
from utils import fopen
from itertools import combinations

def dist(a,b):
    return tuple([abs(i - j) for i,j in zip(a, b)])

def add(a,b):
    return tuple([i + j for i,j in zip(a, b)])

def sub(a,b):
    return tuple([i - j for i,j in zip(a, b)])

def prod(a,b):
    return sum([i * j for i,j in zip(a,b)])

def get_vector(v1, p):
    x = []
    for d in p:
        v = None
        if v1 == d:
            v = 1
        elif v1 == -d:
            v = -1
        else:
            v = 0
        x.append(v)
    return x

def get_map(a, b):
    dx0,dy0,dz0 = a
    return [get_vector(dx0, b), get_vector(dy0, b), get_vector(dz0, b)]

class Intersection:
    def __init__(self, there, here, intersection):
        self.there = there
        self.here = here
        self.intersection = intersection

class Signal:
    def __init__(self, s, i):
        self.t = tuple(map(int, s.split(',')))
        self.i = i
        self.rel = {}

    def align(self, s):
        t = dist(self.t, s.t)
        fp = ("%.2f" % hypot(*t), min(*t), max(*t))
        self.rel[s.i] = s.rel[self.i] = fp

    def intersect(self, sig):
        res = []
        for i,r in self.rel.items():
            k = next((key for key, value in sig.rel.items() if value == r), None)
            if k:
                res.append(tuple([r, i, k]))
        return res

    def adjust(self, p):
        x = prod(self.t, p[0])
        y = prod(self.t, p[1])
        z = prod(self.t, p[2])
        self.t = (x,y,z)

class Scanner:
    def __init__(self, l):
        self.position = None
        self.signals = [Signal(n, i) for i,n in enumerate(l.split('\n')[1:]) if n]
        [x.align(s) for x,s in combinations(self.signals,2)]

    def align(self, sc, data):
        for line in data.intersection:
            if line[0][1] == 0:
                continue
            h = self.signals[line[2]]
            dh = sub(data.here.t, h.t)
            dx0, dy0, dz0 = dh
            if abs(dx0) == abs(dy0) or abs(dz0) == abs(dy0) or abs(dx0) == abs(dz0):
                continue
            t = sc.signals[line[1]]
            dt = sub(data.there.t, t.t)

            mp = get_map(dh, dt)

            for sig in sc.signals:
                sig.adjust(mp)

            sc.position = sub(data.here.t, data.there.t)

            for sig in sc.signals:
                sig.t = add(sig.t, sc.position)

            break

        return None

    def intersect(self, sc):
        for there in sc.signals:
            for here in self.signals:
                i = there.intersect(here)
                if len(i) >= 11:
                    return Intersection(there, here, i)

def align_scanners():
    scanners = [Scanner(l) for l in fopen(19).read().split('\n\n')]
    l = set([0])
    scanners[0].position = (0, 0, 0)
    while len(l) < len(scanners):
        for i,s in enumerate(scanners):
            for j,c in enumerate(scanners):
                if s == c or i not in l or j in l:
                    continue
                intersection = s.intersect(c)
                if intersection:
                    s.align(c, intersection)
                    l.add(j)
    return scanners

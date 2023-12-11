from itertools import combinations
from utils import coords

def expand(g, func):
    cols = set(map(func, g))
    return set(range(0, max(cols))).difference(cols)

def dist(p):
    a,b = p
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

def path_sum(m):
    c = list(coords(11, '#').keys())
    cols = expand(c, lambda p: int(p.imag))
    rows = expand(c, lambda p: int(p.real))
    for i,p in enumerate(c):
        co = sum(x < p.imag for x in cols)
        ro = sum(x < p.real for x in rows)
        c[i] += (1j * co * m) + (ro * m)
    return int(sum(map(dist, combinations(c, 2))))

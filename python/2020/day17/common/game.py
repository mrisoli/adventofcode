from collections import Counter
from itertools import product

def count_neighbours(t1, t2):
    return tuple([x + y for x, y in zip(t1, t2)])

def make_round(a, r):
    n = Counter(count_neighbours(p, s) for p in a for s in r)
    out = {p for p in a if n[p] in {2,3}}
    out |= {p for p in set(n.keys()) if n[p] == 3} - a
    return out

def solve(f, d):
    r = set(product(*(range(-1, 2) for _ in range(d))))
    r.discard((0,) * d)
    a = {
        (i, j) + (0,) * (d - 2)
        for i, row in enumerate(f)
        for j, c in enumerate(row)
        if c == "#"
    }
    for _ in range(6):
        a = make_round(a, r)
    return len(a)

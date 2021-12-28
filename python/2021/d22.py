from collections import Counter
from math import prod
from operator import le
from utils import fopen

def vol(c):
    return c[1] - c[0] + 1

def get_coords(x, m):
    l,h = list(map(int,x[2:].split('..')))
    if m and (abs(l) > 50 or abs(h) > 50):
        return None
    return (l, h)

def parse(c,m):
    c = tuple(map(lambda x: get_coords(x,m), c.strip().split(',')))
    return c if all(c) else None

def combine(ps):
    p1,p2 = ps
    return (max(p2[0],p1[0]), min(p2[1], p1[1]))

def mxmn(r1, r2):
    return tuple(map(combine, zip(r1, r2)))

def neg(t):
    return all(map(lambda x: le(*x) ,t))

def solve(m=True):
    s = Counter()
    for l in fopen(22).readlines():
        i,c = l.split(' ')
        c = parse(c,m)
        if not c:
            continue
        i = 1 if i == "on" else -1
        u = Counter()
        for e, ie in s.items():
            t = mxmn(c,e)
            if neg(t):
                u[t] -= ie

        if i > 0:
            u[c]+= i
        s.update(u)
    print(sum(prod(map(vol, cube)) * v for cube, v in s.items()))

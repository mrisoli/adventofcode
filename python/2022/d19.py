import re
from operator import sub,add

def parse(l):
    return tuple(map(int, re.findall('\d+', l)))

def c_p(l):
    a,b,c,d,e,f = l
    return (
            ((0, 0, 0, a), (0,0,0,1)),
            ((0, 0, 0, b), (0,0,1,0)),
            ((0, 0, d, c), (0,1,0,0)),
            ((0, f, 0, e), (1,0,0,0)),
            ((0, 0, 0, 0), (0,0,0,0)))

def key(a):
    return tuple(map(add, a[0],a[1])) + a[1]

def prune(v):
    return sorted({key(x):x for x in v}.values(), key=key)[-1000:]

def possible(d, cp):
    return [
            (tuple(map(sub, map(add,h, m), cost)), tuple(map(add, m, prod)))
            for h,m in d for cost,prod in cp
            if all(map(lambda x: x[0] <= x[1], zip(cost, h)))
            ]

def calc(b, t):
    g = 0
    d = [((0,0,0,0), (0,0,0,1))]
    cp = c_p(b)
    for _ in range(t,0,-1):
        d = prune(possible(d, cp))
    return max(h[0] for h,_ in d)

from utils import fopen
from collections import Counter

def points(l, d):
    p1,p2 = l.split('->')
    x1,y1 = map(int, p1.split(','))
    x2,y2 = map(int, p2.split(','))
    if x1 == x2:
        return [(x1, y) for y in range(min(y1,y2),max(y1,y2) + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1,x2),max(x1,x2) + 1)]
    elif d:
        dx = 1 if x1 < x2 else -1
        dy = 1 if y1 < y2 else -1
        return [(x1 + (i * dx), y1 + (i * dy)) for i in range(abs(x2 - x1) + 1)]
    return []

def solve(d=False):
    p = Counter()
    [p.update(points(l, d)) for l in fopen(5).readlines()]
    print(sum(c > 1 for c in p.values()))

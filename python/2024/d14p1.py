from math import prod
from utils import rows_of_int

def parse(l):
    x, y, vx, vy = l
    return (y + (1j * x), vy + (1j *vx))

f = list(map(parse, rows_of_int(14)))
mx = int(max(f, key=lambda x: x[0].real)[0].real) + 1
my = int(max(f, key=lambda x: x[0].imag)[0].imag) + 1

def get_pos(mx, my, p,v):
    pn = p + 100 * v
    px = pn.real % mx if pn.real > 0 else (mx + (pn.real % mx)) % mx
    py = pn.imag % my if pn.imag > 0 else (my + (pn.imag % my)) % my
    pn = (px + 1j * py)
    return (pn, v)

def quadrant(ps, hx, hy, x, y):
    return sum(1 for p in ps if p.real in range(hx * x, hx * (x + 1) + 1) and p.imag in range(hy * y, hy * (y + 1) + 1))

def calc(f):
    hx, hy = mx // 2, my // 2
    ps = [p for p,v in f if p.real != hx and p.imag != hy]
    q = []
    for x in range(2):
        for y in range(2):
            q.append(quadrant(ps, hx, hy, x, y))
    return prod(q)


print(calc([get_pos(mx, my, p,v) for p,v in f]))


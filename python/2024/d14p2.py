from math import prod
from utils import rows_of_int

def parse(l):
    x, y, vx, vy = l
    return (y + (1j * x), vy + (1j *vx))

f = list(map(parse, rows_of_int(14)))
mx = int(max(f, key=lambda x: x[0].real)[0].real) + 1
my = int(max(f, key=lambda x: x[0].imag)[0].imag) + 1

def get_pos(mx, my, p,v):
    pn = p + v
    px = pn.real % mx if pn.real > 0 else (mx + (pn.real % mx)) % mx
    py = pn.imag % my if pn.imag > 0 else (my + (pn.imag % my)) % my
    pn = (px + 1j * py)
    return (pn, v)

def pprint(ps):
    hx, hy = mx // 2, my // 2
    for x in range(mx):
        for y in range(my):
            c = ps.count(x + (y * 1j))
            if c == 0:
                print('.', end='')
            else:
                print(c, end='')
        print()

def find_seq(f):
    s = set(f)
    h,v = False, False
    for x in range(mx):
        for y in range(my):
            if all([x + n + (1j * y) in s for n in range(10)]) and all([x + (1j * (y + n)) in s for n in range(-5,5,1)]):
                return True
    return h and v

i = 0
while not find_seq([p for p,v in f]):
    f = [get_pos(mx, my, p,v) for p,v in f]
    i += 1

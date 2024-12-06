from utils import coords

DIRECTION = [-1, 1j, 1, -1j]

def setup():
    f = coords(6, tokens='^#.')
    s = next(k for k,v in f.items() if v == '^')
    return f, s

def next_dir(d):
    return DIRECTION[(DIRECTION.index(d) + 1) % 4]

def run(f, s, p):
    if f.get(s + p) == '#':
        return s, next_dir(p)
    else:
        return s + p, p
    return s

def solve(f, s):
    p = -1
    c = set()
    while s in f:
        c.add(s)
        s,p = run(f, s, p)
    return c

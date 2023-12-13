from utils import obj_list, coords

def transpose(g):
    return set(map(lambda x: x.imag + 1j * x.real, g))

def dots(g, n):
    return set(map(lambda x: int(x.real), filter(lambda x: int(x.imag) == n, g)))

def expand_line(g, a, b, s):
    c1, c2 = dots(g, a), dots(g, b)
    if c1 == c2:
        return expand_line(g, a + 1, b - 1, s)
    if s and len(c1 ^ c2) == 1 and len(c1 & c2) > 0:
        return expand_line(g, a + 1, b - 1, False)
    return not s and (len(c1) == 0 or len(c2) == 0)

def traverse(g, s):
    m = max([int(c.imag) for c in g])
    for i in range(1, m + 1):
        if expand_line(g, i, i - 1, s):
            return i

def solve(g, s):
    return traverse(g, s) or (100 * traverse(transpose(g), s))

def run(s=False):
    return sum(map(lambda g: solve(g, s), [coords(x, '#').keys() for x in [f.split('\n') for f in obj_list(13)]]))

from d12 import border, NEIGHBORS, solve

def count_groups(l, v):
    if len(l) == 0:
        return 0
    s = sorted(l, key=lambda x: (x.real, x.imag))
    return 1 + sum(1 for a, b in zip(s, s[1:]) if not b - a == v)

def count_sides(a):
    minx = min(map(lambda x: int(x.real), a))
    miny = min(map(lambda y: int(y.imag), a))
    maxx = max(map(lambda x: int(x.real), a))
    maxy = max(map(lambda y: int(y.imag), a))
    sides = 0
    # top
    for x in range(minx, maxx + 1):
        ps = list(filter(lambda v: v.real == x and v - 1 not in a, a))
        s = count_groups(ps, 1j)
        sides += s
    # right
    for y in range(miny, maxy + 1):
        ps = list(filter(lambda v: v.imag == y and v + 1j not in a, a))
        s = count_groups(ps, 1)
        sides += s
    # bottom
    for x in range(minx, maxx + 1):
        ps = list(filter(lambda v: v.real == x and v + 1 not in a, a))
        s = count_groups(ps, 1j)
        sides += s
    # left
    for y in range(miny, maxy + 1):
        ps = list(filter(lambda v: v.imag == y and v - 1j not in a, a))
        s = count_groups(ps, 1)
        sides += s
    return sides

def sides(f, a, v):
    c = count_sides(a)
    return c

solve(sides)

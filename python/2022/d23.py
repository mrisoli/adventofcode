from collections import Counter,deque
from utils import coords

def get_new_pos(f, m):
    new_positions = {}
    for el in f:
        adj = {v for dr in m for v in get_adjacencies(el, dr)}
        dr = next(filter(lambda dr: all(map(lambda x: x not in f, get_adjacencies(el, dr))), m), None)
        if dr is not None and len(adj & f) > 0:
            new_positions[el] = el + dr
    return new_positions


def get_adjacencies(v, n):
    c = 1j if n.real != 0 else 1
    return  (v + n - c, v + n, v + n + c)

def rnd(f,m):
    np = get_new_pos(f, m)
    c = Counter(np.values())
    r = {k:v for k, v in np.items() if c[v] == 1}
    m.rotate(-1)
    f -= r.keys()
    return f | set(r.values())

def get_coords():
    return coords(23, '#'), deque([-1, 1, -1j, +1j])

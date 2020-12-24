from common import tiles
from copy import deepcopy

def get_neighbours(i, j):
    w = (i, j - 2)
    e = (i, j + 2)
    nw = (i - 1, j - 1)
    ne = (i - 1, j + 1)
    sw = (i + 1, j - 1)
    se = (i + 1, j + 1)
    return [w, e, nw, ne, sw, se]

def count_neighbours(h, i, j):
    t = 0
    for v in get_neighbours(i, j):
        (ii, jj) = v
        if h.get(ii, {}).get(jj, False):
            t += 1
    return t

def fill(h):
    cp = deepcopy(h)
    for i,r in h.items():
        for j in r.keys():
            for v in get_neighbours(i, j):
                (ii, jj) = v
                if ii not in cp:
                    cp[ii] = {}
                if jj not in cp[ii]:
                    cp[ii][jj] = False
    return cp

def run(h):
    cp = fill(h)
    for i,r in cp.items():
        for j,c  in r.items():
            t = count_neighbours(h,i,j)
            if (c and (t == 0 or t > 2)) or (not(c) and t == 2):
                cp[i][j] = not(c)
    return cp

f = open('p.in').read().splitlines()
h = tiles.get_grid(f)
for _ in range(100):
    h = run(h)
print(tiles.count_tiles(h))

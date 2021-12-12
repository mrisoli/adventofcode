from utils import int_grid
from heapq import nlargest
from functools import reduce
from operator import mul
from d9 import get_neighbors

def get_neighbors_idx(g, i, j):
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [(ix,jx) for (ix, jx) in neighbors if ix >= 0 and ix < len(g) and jx >= 0 and jx < len(g[i])]

def get_basin(g, i, j, visited, tovisit):
    visited.add(tuple([i, j]))
    n = set([(ix,jx) for ix, jx in get_neighbors_idx(g, i, j) if g[ix][jx] != 9])
    tovisit = tovisit.union(n - visited)
    if len(tovisit) == 0:
        return 1
    else:
        ti, tj = tovisit.pop()
        return 1 + get_basin(g, ti, tj, visited, tovisit)

g,b = int_grid(9),[]
for i in range(len(g)):
    for j in range(len(g[i])):
        v,n = g[i][j], get_neighbors(g, i, j)
        if all(map(lambda x: x > v, n)):
            b.append(get_basin(g, i, j, set(), set()))

print(reduce(mul, nlargest(3, b)))

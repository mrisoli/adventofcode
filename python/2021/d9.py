def get_neighbors(g, i, j):
    neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    return [g[ix][jx] for ix, jx in neighbors if ix >= 0 and ix < len(g) and jx >= 0 and jx < len(g[i])]

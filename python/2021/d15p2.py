from utils import int_grid
from d15 import solve

def gen_grid(g):
    l = len(g)
    lg = 5 * l
    gg = [[0 for x in range(lg)] for j in range(lg)]
    for i in range(lg):
        for j in range(lg):
            gg[i][j] = g[i % l][j % l] + (i // l) + (j // l)
            if gg[i][j] > 9:
                gg[i][j] -= 9
    return gg

g = int_grid(15)
solve(gen_grid(int_grid(15)))

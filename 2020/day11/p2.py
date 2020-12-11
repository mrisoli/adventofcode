from copy import deepcopy
from common import seat

def check_direction(m, i, j, di, dj):
    ii,jj = i + di, j + dj
    while 0 <= ii < len(m) and 0 <= jj < len(m[ii]):
        if m[ii][jj] == '.':
            ii += di
            jj += dj
            continue
        elif m[ii][jj] == '#':
            return True
        else:
            return False
    return False

def sights(m, i, j):
    o = 0
    r = [-1, 0, 1]
    for di in r:
        for dj in r:
            if di == 0 and dj == 0:
                continue
            if check_direction(m, i, j, di, dj):
                o += 1
    return o

seat.solve_with(5, sights)

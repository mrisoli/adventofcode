from functools import cache
from utils import coords,hash_dict

def max_col(f):
    return max(int(k.imag) for k in f.keys())

def max_row(f):
    return max(int(k.real) for k in f.keys())

def col(g, n):
    return {k: v for k, v in g.items() if k.imag == n}

def rocks(g):
    return sorted([k for k, v in g.items() if v == 'O'], key=lambda x: x.real)

def calc(f):
    m = max(int(k.real) for k in f.keys())
    return sum([int(m - k.real + 1) for k, v in f.items() if v == 'O'])

@hash_dict
@cache
def rotate(f):
    mr = max_row(f)
    return {int(k.imag) + ((mr - k.real) * 1j):v for k, v in f.items()}

@hash_dict
@cache
def lever(f):
    m = max(int(k.imag) for k in f.keys())
    for i in range(m + 1):
        cl = col(f, i)
        rs = rocks(cl)
        for r in rs:
            cl = col(f, i)
            fl = max([int(x.real) for x in cl if x.real < r.real], default=None)
            if fl is not None:
                f[fl + 1 + (i * 1j)] = f.pop(r)
            else:
                f[(i * 1j)] = f.pop(r)
    return f

def make():
    return coords(14, '#O')

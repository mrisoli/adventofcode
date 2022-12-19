from utils import fopen
from itertools import cycle

rocks = [
        (0, (0,1,2,3)),
        (2, (1,0+1j,2+1j,1+2j)),
        (2, (0,1,2,2+1j,2+2j)),
        (3, (0,0+1j,0+2j,0+3j)),
        (1, (0,1,0+1j,1+1j)),
        ]

def get_rocks():
    return cycle(enumerate(rocks))

def empty(b, p):
    return p.real in range(7) and p.imag > 0 and p not in b

def check(b, p, r, d):
    return all(empty(b, p + d + ro) for ro in r)

def directions():
    return cycle([(i, ord(x) - 61) for i,x in enumerate(fopen(17).read().strip())])

def run(v):
    c = directions()
    rocks = get_rocks()
    b, cache, t = set(), {}, 0
    j = 0
    for s in range(v):
        p = complex(2, t + 4)
        i, (h, rock) = next(rocks)

        if v > 2022:
            k = i,j
            if k in cache:
                ss,tt = cache[k]
                d, m = divmod(v - s, s - ss)
                if m == 0:
                    return t + (t - tt) * d
            else: cache[k] = s,t
        while True:
            j, d = next(c)
            if check(b, p, rock,  d): p += d
            if check(b, p, rock,-1j): p += -1j
            else: break
        b |= {p + r for r in rock}
        t = int(max(t, p.imag + h))
    return t

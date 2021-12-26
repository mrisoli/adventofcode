from functools import lru_cache
from itertools import product
from utils import int_row

@lru_cache(maxsize=None)
def run(p1, p2, s1, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    a = (0, 0)
    for d in product(range(1, 4), repeat=3):
        np = p1 + sum(d)
        while np > 10:
            np -= 10
        ns = s1 + np

        v2, v1 = run(p2, np, s2, ns)
        a = (a[0] + v1, a[1] + v2)
    return a

p1, p2 = int_row(21)

print(max(run(p1, p2, 0, 0)))

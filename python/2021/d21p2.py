from functools import lru_cache
from itertools import product
from utils import int_row

@lru_cache(maxsize=None)
def run(p1, p2, s1, s2):
    if max(s1, s2) >= 21:
        return (int(s1 >= 21), int(s2 >= 21))
    a = (0, 0)
    for d in product([1, 2, 3], repeat=3):
        np = p1 + sum(d)
        if np > 10:
            np -= 10

        v2, v1 = run(p2, np, s2, s1 + np)
        a = (a[0] + v1, a[1] + v2)
    return a

p1, p2 = int_row(21)

print(max(run(p1, p2, 0, 0)))

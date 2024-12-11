from functools import lru_cache
from utils import int_row

def rule(n):
    s = str(n)
    if n == 0:
        return [1]
    elif len(s) % 2 == 0:
        return [int(s[:len(s)//2]) , int(s[len(s)//2:])]
    return [n * 2024]

@lru_cache(maxsize=None)
def rectransform(n, i):
    if i == 0:
        return 1
    return sum([rectransform(r, i-1) for r in rule(n)])

def recsolve(n):
    f = int_row(11, separator=' ')
    print(sum([rectransform(i, n) for i in f]))

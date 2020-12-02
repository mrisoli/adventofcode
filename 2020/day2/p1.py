from functools import reduce
import re

def valid(s):
    [l, h, c, p] = re.match(r'(\d+)-(\d+) (\w+): (\w+)', s).groups()
    l, h = int(l), int(h)
    return l <= p.count(c) <= h

with open('puzzle.in') as f:
    print(reduce(lambda t, s: t + (1 if valid(s) else 0), f.readlines(), 0))

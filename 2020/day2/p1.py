import re

def valid(s):
    [l, h, c, p] = re.match(r'(\d+)-(\d+) (\w+): (\w+)', s).groups()
    l, h = int(l), int(h)
    return l <= p.count(c) <= h

with open('puzzle.in') as f:
        print(len(list(filter(valid, f.readlines()))))

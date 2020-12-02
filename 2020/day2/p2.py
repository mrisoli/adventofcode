import re

def valid(s):
    [l, h, c, p] = re.match(r'(\d+)-(\d+) (\w+): (\w+)', s).groups()
    l, h = int(l) - 1, int(h) - 1
    return [p[l], p[h]].count(c) == 1

with open('puzzle.in') as f:
        print(len(list(filter(valid, f.readlines()))))

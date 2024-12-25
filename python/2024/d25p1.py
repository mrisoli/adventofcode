from itertools import groupby
from utils import obj_list

def build(x, c):
    g = set()
    for ln,line in enumerate(x.split('\n')):
        for cn,cell in enumerate(line):
            if cell == c:
                g.add(complex(ln,cn))
    return g

def heights(x):
    t = []
    for i in range(5):
        t.append(int(max([c.real for c in x if c.imag == i])))
    return t

f = sorted(obj_list(25))
t = []
for k,g in groupby(f, lambda x: x[0]):
    t.append(list(g))
[locks, keys] = t
keys = [heights(build(k, '.')) for k in keys]
locks = [heights(build(k, '#')) for k in locks]
t = 0
for l in locks:
    for k in keys:
        p = [b - a for a,b in zip(l,k)]
        if all([x >= 0 for x in p]):
            t += 1
print(t)

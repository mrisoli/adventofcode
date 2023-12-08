from math import lcm
from d8 import init

d, nodes = init()
c = list(filter(lambda s: s.endswith('A'), nodes.keys()))
a = [None] * len(c)
t = 0
s = 0
while not all(a):
    t += 1
    dr = d[s]
    s = (s + 1) % len(d)
    if dr == 'L':
        c = [nodes[n].left for n in c]
    elif dr == 'R':
        c = [nodes[n].right for n in c]
    for i,n in enumerate(c):
        if n.endswith('Z') and not a[i]:
            a[i] = t
print(lcm(*a))

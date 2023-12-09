from math import lcm
from d8 import init,find

d, n = init()
c = list(filter(lambda s: s.endswith('A'), n.keys()))
print(lcm(*map(lambda x: find(d, n, x, 'Z'), c)))

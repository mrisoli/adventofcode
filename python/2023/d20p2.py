from math import lcm
from d20 import Solver

s = Solver()

r = []
for m in s.data['broadcaster']:
    nextl = [m]
    n = 0
    l = 0
    while nextl:
        d = nextl[0]
        g = s.data['%' + d]
        n |= (len(g) == 2 or '%' + g[0] not in s.data) << l
        l += 1
        nextl = [next_ for next_ in s.data['%' + d] if '%' + next_ in s.data]
    r.append(n)
print(lcm(*r))

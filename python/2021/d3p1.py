from utils import str_list
from collections import Counter

l = str_list(3)
t = [list(r) for r in zip(*l)]

g = []
e = []

for n in t:
    c = Counter(n)
    gg = c.most_common(1)[0][0]
    ee = c.most_common(2)[1][0]
    g.append(gg)
    e.append(ee)
g = int(''.join(g), 2)
e = int(''.join(e), 2)
print(g * e)

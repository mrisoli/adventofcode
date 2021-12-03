from utils import str_list
from collections import Counter

g,e = [],[]

for n in zip(*str_list(3)):
    gg, ee = Counter(n).most_common(2)
    g.append(gg[0])
    e.append(ee[0])
print(int(''.join(g), 2) * int(''.join(e), 2))

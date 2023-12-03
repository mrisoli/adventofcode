from collections import defaultdict
from d3 import generate

gears = defaultdict(list)
[gears[t].append(n) for t,n in generate(r'[*]')]
print(sum(x[0] * x[1] for x in gears.values() if len(x) == 2))

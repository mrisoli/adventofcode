from d16 import generate
from functools import cache
from collections import defaultdict

r = {}
d = defaultdict(lambda: 1000)
r,d = generate()

@cache
def visit(t, l='AA', vs=frozenset(r), e=False):
    return max([r[u] * (t - d[u,l] - 1) + visit(t - d[u,l] - 1, u, vs - {u}, e)  for u in vs if d[u,l] < t] + [visit(26, vs=vs) if e else 0])
print(visit(26, e=True))

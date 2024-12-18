from heapq import heappop, heappush
from utils import coords

f = coords(16)
r = next(k for k,v in f.items() if v == 'S')
e = next(k for k,v in f.items() if v == 'E')

class Vertex:
    def __init__(self, val, path=set()):
        self.val = val
        self.path = path | {val}

    def __lt__(self, other):
        return False

DIRS = [-1, 1j, 1, -1j]
q = [(0, Vertex(r), 1j)]
v = set()
m = 10**9
s = set()
while q:
    dist, pos, d = heappop(q)
    v.add((pos.val, d))
    if pos.val == e:
        if dist <= m:
            m = dist
            s |= set(pos.path)
    if f.get(pos.val + d) != '#' and (pos.val + d, d) not in v:
        heappush(q, (dist + 1, Vertex(pos.val + d, pos.path), d))
    for nd in [d*-1j,d*1j]:
        np = pos.val + nd
        if f.get(np) != '#' and (np, nd) not in v:
            heappush(q, (dist + 1001, Vertex(np, pos.path), nd))
print(len(s))

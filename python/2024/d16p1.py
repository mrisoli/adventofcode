from heapq import heappop, heappush
from utils import coords

f = coords(16)
r = next(k for k,v in f.items() if v == 'S')
e = next(k for k,v in f.items() if v == 'E')

class Vertex:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return False

DIRS = [-1, 1j, 1, -1j]
q = [(0, Vertex(r), 1j)]
v = set()
while q:
    dist, pos, d = heappop(q)
    if pos.val == e:
        print(dist)
        break
    if f.get(pos.val + d) != '#' and (pos.val, d) not in v:
        v.add((pos.val, d))
        heappush(q, (dist + 1, Vertex(pos.val + d), d))
    for nd in [d*-1j,d*1j]:
        np = pos.val + nd
        if f.get(np) != '#' and (np, nd) not in v:
            v.add((np, d))
            heappush(q, (dist + 1001, Vertex(np), nd))

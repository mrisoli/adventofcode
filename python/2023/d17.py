from heapq import heappush, heappop, merge
from utils import coords

class Vertex:
    def __init__(self, val: complex):
        self.val = val

    def __get__(self):
        return self.val

    def __set__(self, val):
        self.val = val

    def __repr__(self):
        return f'{(int(self.val.real), int(self.val.imag))}'

    def __lt__(self, other):
        return False

type State = tuple[int, Vertex, complex]
type Point = tuple[complex, int]

def vector(d: complex) -> complex:
    m = 1j if d.imag != 0 else 1
    return -m if d.real + d.imag < 0 else m

def size(v: complex) -> int:
    return int(abs(v.real + v.imag))


class Solver:
    def __init__(self, mn: int, mx: int):
        self.g = coords(17, ''.join(map(str, range(10))), lambda x: int(x))
        self.target = max(self.g.keys(), key=lambda x: int(x.imag)) + max(self.g.keys(), key=lambda x: int(x.real))
        self.mn = mn
        self.mx = mx


    def neighbours(self, u: State) -> [State]:
        c, p, v = u
        ss = vector(v.imag + (1j * v.real))
        ss = [-ss, ss]
        ss.append(v + vector(v))
        a = []
        for vs in ss:
            ps = p.val + vector(vs)
            if ps in self.g and size(vs) <= self.mx:
                a.append((c + self.g[ps], Vertex(ps), vs))
        return a

    def djikstra(self) -> int:
        q: list[State] = [
            (self.g[1], Vertex(1), 1),
            (self.g[1j], Vertex(1j), 1j),
        ]
        v = set()
        s = float('inf')
        while q:
            u = heappop(q)
            cost, pos, dr = u
            if pos.val == self.target:
                return cost
            if (pos.val, dr) in v:
                continue
            v.add((pos.val, dr))
            for n in self.neighbours(u):
                heappush(q, n)

#def jrange(p1: complex, p2: complex):
    #d = p2 - p1
    #m = vector(d)
    ##d = int(abs(d.real + d.imag))
    #for i in range(1, d + 1):
    #    yield i * m

    #def loss(self, a, b ) -> int:
        #pa, _ = a
        #pb, _ = b
        #return sum(self.g[pa + v] for v in jrange(pa,pb))

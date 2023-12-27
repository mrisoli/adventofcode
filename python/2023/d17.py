from heapq import heappush, heappop, merge
from utils import coords

type State = tuple[int, Vertex, complex]

def vector(d: complex) -> complex:
    m = 1j if d.imag != 0 else 1
    return -m if d.real + d.imag < 0 else m

def size(v: complex) -> int:
    return int(abs(v.real + v.imag))

class Vertex:
    def __init__(self, val: complex):
        self.val = val

    def __repr__(self):
        return f'{(int(self.val.real), int(self.val.imag))}'

    def __lt__(self, other):
        return False

class Solver:
    def __init__(self, mn: int, mx: int):
        self.g = coords(17, ''.join(map(str, range(10))), lambda x: int(x))
        self.target = max(self.g.keys(), key=lambda x: size(x))
        self.min = mn
        self.max = mx

    def djikstra(self) -> int:
        q: list[State] = [
            (self.g[1], Vertex(1), 1),
            (self.g[1j], Vertex(1j), 1j),
        ]
        v = set()
        while q:
            u = heappop(q)
            cost, pos, direction = u
            if pos.val == self.target and size(direction) >= self.min:
                return cost
            if (pos.val, direction) in v:
                continue
            v.add((pos.val, direction))
            turn = vector(direction.imag + (1j * direction.real))
            ps = pos.val - turn
            if ps in self.g and size(direction) >= self.min:
                heappush(q, (cost + self.g[ps], Vertex(ps), -turn))
            ps = pos.val + turn
            if ps in self.g and size(direction) >= self.min:
                heappush(q, (cost + self.g[ps], Vertex(ps), turn))
            ps = pos.val + vector(direction)
            step_forward = direction + vector(direction)
            if ps in self.g and size(step_forward) <= self.max:
                heappush(q, (cost + self.g[ps], Vertex(ps), step_forward))

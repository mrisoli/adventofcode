from utils import str_list, polygon_area

type Plan = tuple[str, str]
type Draft = tuple[Plan, str]

D = {'R': 1j, 'L': -1j, 'U': -1, 'D': 1}

def dig(p: complex, c: Plan) -> set[complex]:
    d, n = c
    return [p := p + D[d] for i in range(int(n))]

def parse(t: str) -> Draft:
    d, n, c = tuple(t.split(' '))
    return ((d, n), c)

def make():
    return list(map(parse, str_list(18)))

def solve(z: list[Plan]) -> int:
    cp = 0
    g = [cp]
    for x in z:
        d = dig(cp, x)
        cp = d[-1]
        g += d
    return len(g) + polygon_area(g)

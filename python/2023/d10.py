from utils import coords

MOVES = {
        'S': [-1, -1j, 1],
        'L': [-1, 1j],
        'J': [-1, -1j],
        '7': [-1j, 1],
        'F': [1, 1j],
        '|': [-1, 1],
        '-': [-1j, 1j],
}

def parse(tokens):
    return dict(coords(10, tokens))

def neighbors(g, n):
    return [n + m for m in MOVES[g[n]]]

def get_polygon():
    g = parse('|-LJ7FS')
    s = list(g.keys())[list(g.values()).index('S')]
    n = next(x for x in neighbors(g,s) if x in g)
    p = [s]
    while(n != s):
        p.append(n)
        n = next(x for x in neighbors(g,n) if x != p[-2])
    return p

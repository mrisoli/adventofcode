from utils import coords

DIRECTIONS = [1, 1j, -1, -1j, 1+1j, -1+1j, -1-1j, 1-1j]
g = coords(4)

def get(k, v):
    return ''.join(g.get(k + l * v, '.') for l in range(4))

def parse(k):
    return sum(get(k, v) == 'XMAS' for v in DIRECTIONS)

print(sum(parse(k) for k,v in g.items() if v == 'X'))

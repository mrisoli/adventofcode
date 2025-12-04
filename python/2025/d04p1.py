from utils import coords

NEIGHBORS = [-1,-1j,1,1j,-1-1j,-1+1j,1-1j,1+1j]

def accessible(g, p):
    return sum(1 for n in NEIGHBORS if p + n in g) < 4

g = coords(4, tokens='@').keys()

print(sum(1 for p in g if accessible(g, p)))

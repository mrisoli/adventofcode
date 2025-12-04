from utils import coords

NEIGHBORS = [-1,-1j,1,1j,-1-1j,-1+1j,1-1j,1+1j]

def accessible(g, p):
    return sum(1 for n in NEIGHBORS if p + n in g) < 4

g = coords(4, tokens='@').keys()

t = 0
while True:
    removables = set(filter(lambda p: accessible(g, p), g))
    if len(removables) == 0:
        break
    t += len(removables)
    g -= removables
print(t)

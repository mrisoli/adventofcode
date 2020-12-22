from common import image
from math import prod

def flip(t):
    flipped = [s[::-1] for s in t]
    return flipped[::-1]

f = open('p.in').read().splitlines()
tiles = image.get_tiles(f)
edges = {}
for n,t in tiles.items():
    edges[n] = image.get_borders(t)
    edges[-n] = flip(image.get_borders(t))

print(prod([t for t,a in edges.items() if len(image.edges(edges, t, a)) == 2]))

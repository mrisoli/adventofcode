from common import tiles

f = open('p.in').read().splitlines()
h = tiles.get_grid(f)
print(tiles.count_tiles(h))

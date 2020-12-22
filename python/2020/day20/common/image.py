def get_borders(grid):
    top = grid[0]
    bottom = grid[-1]
    left = ''.join(map(lambda x: x[0], grid))
    right = ''.join(map(lambda x: x[-1], grid))
    return [top,right,bottom,left]

def flip(t):
    return list(map(lambda s: ''.join(s), zip(t[::-1])))

def border_flip(t):
    return t[::-1]

def get_tiles(l):
    t = {}
    for i in range(0, len(l), 12):
        n = int(''.join(filter(str.isdigit, l[i])))
        t[n] = l[(i + 1):(i + 11)]
    return t

def edges(tiles, t, borders):
    other_tiles = { i:tiles[i] for i in tiles if abs(i) != t }
    other_borders = set([item for sublist in other_tiles.values() for item in sublist])
    return set(borders) - set(other_borders)

from common import image
from copy import deepcopy

monster = set([(0,18), (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19), (2,1), (2,4),(2,7),(2,10),(2,13),(2,16)])

attachment_connections = [2,3,0,1]

def get_flipped_rotations(t):
    return {t: all_rotations(t), -t: all_rotations(-t)}

def all_rotations(t):
    return [get_rotation(t, i) for i in range(4)]

def get_rotation(tile, orientation):
    tt = tiles[abs(tile)]
    if tile < 0:
        tt = image.border_flip(tt)
    return rotate(tt, orientation)

def attach_cell(t, i, j, r, a):
    ii, jj = i, j
    if a == 0:
        ii = i - 1
        if ii not in grid:
            grid[ii] = {}
    elif a == 1:
        jj = j + 1
    elif a == 2:
        ii = i + 1
        if ii not in grid:
            grid[ii] = {}
    elif a == 3:
        jj = j - 1
    s = grid.get(ii, {}).get(jj)
    if not(grid.get(ii, {}).get(jj)):
        grid[ii][jj] = (t, r)
        return True
    else:
        return False

def fit_to(t,c,i,j):
    top = (i - 1, j)
    right = (i, j + 1)
    bottom = (i + 1, j)
    left = (i, j - 1)
    available_spots = set()
    for x,v in enumerate([top, right, bottom, left]):
        (ii,jj) = v
        if not(grid.get(ii, {}).get(jj)):
            available_spots.add(x)
    (tile_number, orientation) = c
    rotated_tile = get_rotation(tile_number, orientation)
    borders = image.get_borders(rotated_tile)
    borders = {av:borders[av] for av in available_spots}
    rotations = get_flipped_rotations(t)
    for k,v in borders.items():
        for u, rots in rotations.items():
            for r,rot in enumerate(rots):
                rot_b = image.get_borders(rot)
                if rot_b[attachment_connections[k]] == v:
                    uu = attach_cell(u, i, j, r, k)
                    if uu:
                        return True
    return False

def find(t):
    for i,row in grid.items():
        for j,cell in row.items():
            if fit_to(t,cell,i,j):
                return True
    return False

def rotate(img, a = 1):
    for _ in range(a):
        img = list(zip(*img[::-1]))
    return [''.join(i) for i in img]

def trim(img):
    return [i[1:-1] for i in img[1:-1]]

def transform(c):
    img = deepcopy(tiles[abs(c[0])])
    if c[0] < 0:
        img = image.flip(img)
    img = rotate(img, c[1])
    img = trim(img)
    return img

def replace(grid):
    im = [[None] * len(grid) for _ in range(len(grid))]
    row_min = abs(min(grid.keys()))
    for r,v in grid.items():
        col_min = abs(min(v.keys()))
        for c,x in v.items():
            im[r + row_min][c + col_min] = transform(x)
    return im

def convert(grid):
    g = [''] * (8 * len(grid))
    for i,c in enumerate(grid):
        for j,v in enumerate(c):
            for k,x in enumerate(v):
                g[(8 * i) + k] += x
    return g

def find_monster(grid):
    gridb = deepcopy(grid)
    for _ in range(4):
        counter = 0
        gridcp = deepcopy(gridb)
        gridcp = [list(g) for g in gridcp]
        for i in range(0, len(gridcp) - 2):
            for j in range(0, len(gridcp) - 19):
                if all(gridcp[i + m][j + n] == '#' for (m, n) in monster):
                    counter += 1
                    for (m,n) in monster:
                        gridcp[i + m][j + n] = 'O'
        if counter > 0:
            return gridcp
        gridb = rotate(gridb)
    return False

f = open('p.in').read().splitlines()
tiles = image.get_tiles(f)
r_t = set(tiles.keys())
first = min(r_t)
grid = { 0: {0: (first, 0) } }
r_t.remove(first)
while r_t:
    for t in r_t:
        neighbour_data = find(t)
        if neighbour_data:
            r_t.remove(t)
            break

grid = replace(grid)
grid = convert(grid)
grid_with_monster = find_monster(grid)
if not(grid_with_monster):
    grid_with_monster = find_monster(image.flip(grid))
gridcp = [''.join(g) for g in grid_with_monster]
grid = [item for sublist in gridcp for item in sublist]
print(grid.count('#'))

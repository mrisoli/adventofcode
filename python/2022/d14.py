from utils import str_list

def rs(*p):
    return range(min(p), max(p) + 1)

def get_floor(grid):
    return  max([y for _,y in grid])

def get_line(p1,p2):
    return [(x,y) for x in rs(p1[0],p2[0]) for y in rs(p1[1],p2[1])]

def make_grid():
    lines = [[tuple(map(int, p.split(','))) for p in v] for v in map(lambda s: s.split('->'), str_list(14))]
    grid = set()
    for l in lines:
        for p1,p2 in zip(l[:-1], l[1:]):
            points = get_line(p1,p2)
            grid.update(points)
    return grid

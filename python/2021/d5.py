from utils import fopen

def get_lines(f):
    ll = []
    for c in f.readlines():
        ll.append(tuple(map(lambda x: tuple(map(int, x.split(','))), c.split('->'))))
    return ll

def get_diagonal(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1
    x,y = x1,y1
    s = set()
    s.add((x,y))
    while x != x2 and y != y2:
        x += dx
        y += dy
        s.add((x,y))
    return s

def get_points_between(p1, p2, diagonal):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        y1,y2 = min(y1,y2),max(y1,y2)
        return set(map(lambda y: (x1, y), range(y1, y2 + 1)))
    elif y1 == y2:
        x1,x2 = min(x1,x2),max(x1,x2)
        return set(map(lambda x: (x, y1), range(x1, x2 + 1)))
    return get_diagonal(p1, p2) if diagonal else set()


def solve(diagonal=False):
    f = fopen(5)
    lines = get_lines(f)
    points = set()
    intersection = set()
    for (p1, p2) in lines:
        new_points = get_points_between(p1, p2, diagonal)
        intersection = intersection | (points & new_points)
        points = points | new_points
    print(len(intersection))

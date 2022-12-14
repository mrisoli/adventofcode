from utils import str_list

def rs(*p):
    return range(min(p), max(p) + 1)

def get_floor(g):
    return max([y for _,y in g])

def make_grid():
    lines = [zip(l[:-1], l[1:]) for l in [[tuple(map(int, p.split(','))) for p in v] for v in map(lambda s: s.split('->'), str_list(14))]]
    return set.union(*[set.union(*[set((x,y) for x in rs(p1[0],p2[0]) for y in rs(p1[1],p2[1])) for p1,p2 in l]) for l in lines])

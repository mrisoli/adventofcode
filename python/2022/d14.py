from utils import str_list

def rs(*p):
    return range(min(p), max(p) + 1)

def make_grid():
    lines = [zip(l[:-1], l[1:]) for l in [[tuple(map(int, p.split(','))) for p in v] for v in map(lambda s: s.split('->'), str_list(14))]]
    return set.union(*[set.union(*[set((x,y) for x in rs(p1[0],p2[0]) for y in rs(p1[1],p2[1])) for p1,p2 in l]) for l in lines])

def solve(p1):
    g = make_grid()
    f = max([y for _,y in g])
    r = len(g)
    src = (500,0)
    while src not in g:
        p = src
        while True:
            if p[1] > f:
                if p1:
                    return len(g) - r
                break
            for d in [(p[0], p[1] + 1), (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1)]:
                if d not in g:
                    p = d
                    break
            else: break
        g.add(p)
    return len(g) - r

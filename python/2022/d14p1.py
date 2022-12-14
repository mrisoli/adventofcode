from d14 import make_grid

g,f = make_grid()
c, r = 0,len(g)
while not c:
    p = (500,0)
    while True:
        if p[1] > f:
            if not c: c = len(g)
            break
        for d in [(p[0], p[1] + 1), (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1)]:
            if d not in g:
                p = d
                break
        else: break
    g.add(p)

print(c - r)

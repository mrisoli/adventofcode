from d14 import make_grid

g,f = make_grid()
r = len(g)
src = (500,0)
while src not in g:
    p = src
    while True:
        if p[1] > f:
            break
        for d in [(p[0], p[1] + 1), (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1)]:
            if d not in g:
                p = d
                break
        else: break
    g.add(p)

print(len(g) - r)

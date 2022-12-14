from d14 import make_grid,get_floor

g = make_grid()
floor = get_floor(g)
nf = floor
c, r = 0,len(g)

while nf == floor:
    pos = (500,0)
    while True:
        if pos[1] > floor:
            if not c: c = len(g)
            break
        for dest in [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)]:
            if dest not in g:
                pos = dest
                break
        else: break
    g.add(pos)
    nf = get_floor(g)

print(c - r)

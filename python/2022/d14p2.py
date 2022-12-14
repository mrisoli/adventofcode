from d14 import make_grid,get_floor

g = make_grid()
floor = get_floor(g)
r = len(g)

src = (500,0)
while src not in g:
    pos = src
    while True:
        if pos[1] > floor:
            break
        for dest in [(pos[0], pos[1] + 1), (pos[0] - 1, pos[1] + 1), (pos[0] + 1, pos[1] + 1)]:
            if dest not in g:
                pos = dest
                break
        else: break
    g.add(pos)

print(len(g) - r)

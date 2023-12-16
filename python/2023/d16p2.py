from d16 import Grid

g = Grid([])

dr = [i + (1j * j) for i in range(g.mr) for j in range(g.mc) if i in (0,g.mr-1) or j in (0,g.mc-1)]
beams = []

for p in dr:
    if p.real == 0:
        beams += [(1, p)]
    if p.real == g.mr - 1:
        beams += [(-1, p)]
    if p.imag == 0:
        beams += [(1j, p)]
    if p.imag == g.mc - 1:
        beams += [(-1j, p)]

print(max([g.set_beams([b]).run() for b in beams]))

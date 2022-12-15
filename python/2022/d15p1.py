from itertools import chain
from d15 import generate,val,md

v = val(2_000_000)

def run(v):
    c = []
    vb = set()
    for (ps, pb, d) in generate():
        x,y = ps
        if pb[1] == v: vb.add(pb[0])
        if y == v: vb.add(ps[0])
        if v in range(y - d, y + d + 1):
            i = abs(max(y,v) - min(y,v) - d)
            c.append(range(x - i, x + i + 1))
    return len(set(chain(*c))) - len(vb)

print(run(v))

from d15 import generate,val,md

v = val(4_000_000)

def merge(rs):
    b = []
    for begin,end in sorted(rs):
        if b and b[-1][1] >= begin - 1:
            b[-1] = (b[-1][0], max(b[-1][1], end))
        else:
            b.append(tuple([begin, end]))
    return b

def run(v):
    vr = range(v + 1)
    c = [[] for _ in vr]
    for (ps, pb, d) in generate():
        x,y = ps
        if x in vr: c[y].append(tuple([x, x]))
        if pb[0] in vr: c[y].append(tuple([pb[0], pb[0]]))
        for yy in range(y - d, y + d + 1):
            i = abs(max(y,yy) - min(y,yy) - d)
            if yy in range(len(c)):
                c[yy].append(tuple([max(x - i, 0), min(x + i, v + 1)]))
    for y,xr in enumerate(c):
        xr = merge(xr)
        if len(xr) > 1:
            return (xr[0][1] + 1, y)

x, y = run(v)
print((4_000_000 * x) + y)

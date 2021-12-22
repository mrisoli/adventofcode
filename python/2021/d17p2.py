from utils import fopen

def parse(c):
    el, rng = c.split('=')
    st,end = [int(n) for n in rng.split('..')]
    return (el, (st,end + 1))

def shoot(xv, yv, f):
    xs,xe = f['x']
    ys,ye = f['y']
    cx, cy = 0, 0
    while True:
        cx += xv
        cy += yv
        yv -= 1
        if xv > 0:
            xv -= 1
        if cx in range(xs,xe) and cy in range(ys, ye):
            return True
        if xv == 0 and cy < ys:
            return False

f = dict([parse(c) for c in fopen(17).readline()[13:].split(', ')])
print(sum([1 for x in range(1,350) for y in range(-100,100) if shoot(x, y,f)]))

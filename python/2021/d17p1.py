from utils import fopen

def parse(c):
    el, rng = c.split('=')
    st,end = [int(n) for n in rng.split('..')]
    return (el, (st,end))

def shoot(xv, yv, f):
    xs,xe = f['x']
    ys,ye = f['y']
    cx, cy = 0, 0
    my = 0
    while cx < xe and cy not in range(ys, ye):
        cx += xv
        cy += yv
        if cy > my:
            my = cy
        yv -= 1
        if cx in range(xs,xe) and cy in range(ys, ye):
            return my
        if cx > xe:
            return None
    return 0

def get_max_y(f):
    my = 0
    for x in range(1,100):
        for y in range(1,100):
            high = shoot(x, y, f)
            if high and high > my:
                my = high
    return my

f = dict([parse(c) for c in fopen(17).readline()[13:].split(', ')])
print(get_max_y(f))

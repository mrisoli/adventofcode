import re
from math import sqrt,ceil,floor

def parse_num(v):
    return re.findall('\d+', v.split(':')[1])

def equation(a, b, c):
    d = b * b - 4 * a * c
    vsqrt = sqrt(abs(d))

    l = ((-b + vsqrt)/(2 * a))
    h = ((-b - vsqrt)/(2 * a))
    h = int(h)
    l = int(l) + 1 if l == int(l) else int(l)
    return h - l

def ways(w):
    t, d = w
    return equation(-1, t, -d)

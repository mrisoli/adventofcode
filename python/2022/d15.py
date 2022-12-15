import re
import sys
from utils import str_list

def md(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    x = [x1,x2]
    y = [y1,y2]
    return abs(max(x) - min(x)) + abs(max(y) - min(y))

def val(n):
    return int(sys.argv[-1] if len(sys.argv) > 1 and sys.argv[-1].isnumeric() else n)

def generate():
    l = [*map(lambda s: s.split(':'), str_list(15))]
    for s,b in l:
        ps = tuple(map(int, re.findall(r'-?\d+', s)))
        pb = tuple(map(int, re.findall(r'-?\d+', b)))
        d = md(ps, pb)
        yield (ps, pb, d)

from itertools import groupby
from utils import obj_list

def vertical(m, s, x):
    r,c,d = s
    while True:
        r = (r + x) % len(m)
        if r == -1:
            r = len(m) - 1
        while c >= len(m[r]):
            r = (r + x) % len(m)
        if m[r][c] == '#':
            return None
        elif m[r][c] == '.':
            return (r,c,d)

def horizontal(m, s, x):
    r,c,d = s
    while True:
        c = (c + x) % len(m[r])
        if c == -1:
            c = len(m[r]) - 1
        print(r,c,len(m), len(m[r]))
        if m[r][c] == '#':
            return None
        elif m[r][c] == '.':
            return (r,c,d)

def nav(m,s,v):
    if v == 0:
        return s
    d = s[2]
    dr = 1 if d < 2 else -1
    fn = horizontal if d % 2 == 0 else vertical
    x = fn(m,s,dr)
    if x:
        return nav(m,x, v - 1)
    return s

def turn(m,s,v):
    r,c,d = s
    d = (d + (1 if v == 'R' else - 1)) % 4
    return r,c,d

m,c = obj_list(22)
m = m.splitlines()
s = (0, m[0].index('.'), 0)
for v in [int(''.join(v)) if k else ''.join(v) for k,v in groupby(c.strip(), str.isdigit)]:
    s = nav(m,s,v) if isinstance(v, int) else turn(m,s,v)
print(sum(x*y for x,y in zip([s[0] + 1, s[1] + 1, s[2]],[1000,4,1])))

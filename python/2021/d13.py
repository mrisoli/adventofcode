from utils import fopen

def update(c, v, o):
    return abs(v - (c - v))

def get_updated(c, v, o):
    x, y = c
    if o == 0:
        x = update(x, v, o)
    else:
        y = update(y, v, o)
    return (x,y)

def fold_on(c, v, o):
    fold_in = set(map(lambda x: get_updated(x, v, o), filter(lambda x: x[o] > v, c)))
    fold_to = set(filter(lambda x: x[o] < v, c))
    return fold_to.union(fold_in)

def fold(c, i):
    a, v = i
    o = 0 if a == 'x' else 1
    return fold_on(c, v, o)

def read():
    f = fopen(13)
    c = set()
    l = f.readline()
    while l != '\n':
        c.add(tuple(map(int, l.split(','))))
        l = f.readline()
    i = []
    l = f.readline()
    while l:
        a,v = l.split(' ')[2].split('=')
        i.append(tuple([a, int(v)]))
        l = f.readline()
    return (c,i)

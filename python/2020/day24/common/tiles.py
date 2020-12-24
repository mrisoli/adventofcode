def get_hex(h,p,d):
    (r, c) = p
    if d == 'e':
        c += 2
    elif d == 'w':
        c -= 2
    elif d == 'nw':
        r -= 1
        c -= 1
    elif d == 'ne':
        r -= 1
        c += 1
    elif d == 'sw':
        r += 1
        c -= 1
    elif d == 'se':
        r += 1
        c += 1
    return (r,c)

def get_grid(f):
    h = {0: {0: False}}
    for l in f:
        l = list(l)
        p = (0,0)
        while l:
            d = l.pop(0)
            if d in 'sn':
                d += l.pop(0)
            p = get_hex(h,p,d)
        (r, c) = p
        if r not in h:
            h[r] = {}
        h[r][c] = not(h[r].get(c, False))
    return h

def count_tiles(h):
    return sum(len([x for x in r.values() if x]) for r in h.values())

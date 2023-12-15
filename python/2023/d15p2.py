from d15 import make, parse

def split(line):
    label,n = line.replace('-','=').split('=')
    return label, n or None

def power(box):
    return sum([int(f[1]) * (sn + 1) for sn,f in enumerate(box)])

def stack():
    z = map(split, make())
    boxes = [[] for _ in range(256)]
    for c in z:
        l,v = c
        b = parse(l)
        bi = next((i for i,(bl,bv) in enumerate(boxes[b]) if bl == l), None)
        if v is None:
            if bi is not None:
                del boxes[b][bi]
        elif bi is None:
            boxes[b].append(c)
        else:
            boxes[b][bi] = c
    return boxes

print(sum([(bn + 1) * power(b) for bn,b in enumerate(stack())]))

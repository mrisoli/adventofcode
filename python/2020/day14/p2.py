from itertools import product
import re
mask = ''
mem = {}

def setmask(i):
    global mask
    m = i.split('=')[1].lstrip()
    mask = m

def get_addrs(m):
    masks = []
    for x in product('01', repeat=m.count('X')):
        mask = ''
        ix = 0
        for i,v in enumerate(m):
            if v == 'X':
                mask += x[ix]
                ix += 1
            else:
                mask += v
        masks.append(int(mask, 2))
    return masks

def convert(add, mask):
    a = list('{:036b}'.format(add))
    for i,v in enumerate(mask):
        if v == 'X':
            a[i] = 'X'
        else:
            a[i] = str(int(a[i], 2) | int(v, 2))
    return ''.join(a)

def setmem(i, mask):
    [add, v] = i.split('=')
    add = int(re.search(r'\d+', add).group(0))
    v = int(v)
    add = convert(add, mask)
    addrs = get_addrs(add)
    for a in addrs:
        mem[a] = v

def run(i):
    if i.startswith('mask'):
        setmask(i)
    else:
        setmem(i,mask)

f = open('p.in')
for i in f.read().splitlines():
    run(i)
print(sum(mem.values()))

import re
mask = {}
mem = {}
def setmask(i):
    mask.clear()
    m = i.split('=')[1].lstrip()
    for i,v in enumerate(m[::-1]):
        if v == '0':
            mask[i] = 0
        elif v == '1':
            mask[i] = 1

def setmem(i):
    [add, v] = i.split('=')
    add = re.search(r'\d+', add).group(0)
    v = int(v)
    for i, d in mask.items():
        if d == 0:
            v &= ~(1<<i)
        else:
            v |= (1<<i)
    mem[add] = v

def run(i):
    if i.startswith('mask'):
        setmask(i)
    else:
        setmem(i)

f = open('p.in')
for i in f.read().splitlines():
    run(i)
print(sum(mem.values()))

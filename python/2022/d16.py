from collections import defaultdict
from itertools import product
from utils import str_list

r = {}
d = defaultdict(lambda: 1000)
v = set()
def generate():
    for l in str_list(16):
        rate,tu = l.split(';')
        va,rate = rate.split('=')
        va = va[6:8]
        v.add(va)
        tunnels = [*map(lambda x: x.strip(','), tu.split(' ')[5:])]
        for tu in tunnels:
            d[tu, va] = 1
        if rate != '0': r[va] = int(rate)
    for k,i,j in product(v,v,v):
        d[i,j] = min(d[i,j], d[i,k] + d[k,j])
    return r,d

from itertools import groupby
from utils import fopen

*m,_,c = fopen(22)
ps,dr = m[0].index('.') + 1j, 1j
m = {(x+y*1j): c for x,l in enumerate(m) for y,c in enumerate(l) if c in '.#'}

for v in [int(''.join(v)) if k else ''.join(v) for k,v in groupby(c.strip(), str.isdigit)]:
    match v:
        case 'L': d *= +1j
        case 'R': d *= -1j
        case _:
            for _ in range(int(v)):
                p, d = ps + dr, dr
print(int(sum(x*y for x,y in zip([p.real + 1, p.imag + 1, [1j,1,-1j,-1].index(d)],[1000,4,1]))))

from operator import itemgetter
from d18 import make,solve

C = ['R', 'D', 'L', 'U']

def hex_to_plan(hx):
    n = hx[2:-2]
    d = C[int(hx[-2])]
    return d, int(n, 16)

z = make()
z = map(hex_to_plan, map(itemgetter(1), z))
print(solve(z))

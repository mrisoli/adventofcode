from utils import fopen
from operator import xor as XOR, or_ as OR, and_ as AND

lines = [l.split() for l in fopen(24) if '->' in l]

r = lambda c, y: any(y == x and c in (a, b) for a, x, b, _, _ in lines)

print(*sorted(c for a, x, b, _, c in lines if
    x == "XOR" and all(d[0] not in 'xyz' for d in (a, b, c)) or
    x == "AND" and not "x00" in (a, b) and r(c, 'XOR') or
    x == "XOR" and not "x00" in (a, b) and r(c, 'OR') or
    x != "XOR" and c[0] == 'z' and c != "z45"), sep=',')

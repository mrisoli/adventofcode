from itertools import combinations
from utils import rows_of_int

def area(p):
    a,b = p
    ax,ay = a
    bx, by = b
    return (abs(ax - bx) + 1) * (abs(ay - by) + 1)

f = rows_of_int(9)
print(max(map(area, combinations(f, 2))))

from utils import str_list
from d2 import play,VALS

EQUIV = { 'X': 'A', 'Y': 'B', 'Z': 'C'}

def result(a,b):
    if a == b:
        return 'D'
    if VALS[VALS.index(b) - 1] == a:
        return 'W'
    return 'L'

def calc(v):
    a,b = v
    b = EQUIV[b]
    return play(b, result(a,b))

l = [x.split(' ') for x in str_list(2)]
print(sum(map(calc, l)))

from utils import str_list
from d2 import VALS,play

EQUIV = { 'X': 'L', 'Y': 'D', 'Z': 'W'}

def val(a, b):
    match b:
        case 'X':
            return VALS[VALS.index(a) - 1]
        case 'Y':
            return a
        case 'Z':
            return VALS[(VALS.index(a) + 1) % 3]

def calc(v):
    a,b = v
    return play(val(a,b), EQUIV[b])

l = [x.split(' ') for x in str_list(2)]
print(sum(map(calc, l)))

from utils import str_list

WINS = { 'X': 'C', 'Y': 'A', 'Z': 'B'}
EQUIV = { 'X': 'A', 'Y': 'B', 'Z': 'C'}

def val(b):
    match b:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3

def result(a,b):
    if a == EQUIV[b]:
        return 3
    if WINS[b] == a:
        return 6
    return 0

def calc(v):
    a,b = v
    return result(a,b) + val(b)

l = [x.split(' ') for x in str_list(2)]
print(sum(map(calc, l)))

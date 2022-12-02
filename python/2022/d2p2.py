from utils import str_list


VALS = ['A','B','C']

def val(b):
    match b:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3

def calc(v):
    a,b = v
    match b:
        case 'X':
            return val(VALS[VALS.index(a) - 1])
        case 'Y':
            return 3 + val(a)
        case 'Z':
            return 6 + val(VALS[(VALS.index(a) + 1) % 3])

l = [x.split(' ') for x in str_list(2)]
print(sum(map(calc, l)))

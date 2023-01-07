import re
from utils import str_list

def parse(d, x):
    s = d[x]
    if len(s) == 1:
        return s[0]
    a,o,b = s
    return f'({parse(d, a)}{o}{parse(d, b)})'

    return x
def make(a,b):
    return a,b.split(' ')

d = dict(make(*x.split(': ')) for x in str_list(21))
d['humn'] = ['1j']
d['root'][1] = '-('

c = eval(parse(d, 'root') + ')')
print(-int(c.real / c.imag))

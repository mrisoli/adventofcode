import re
from utils import str_list

def is_valid(co, symbols):
    l, st, end = co
    return next(((r, c) for r in range(l - 1, l + 2) for c in range(st - 1, end + 1) if (r,c) in symbols), None)

def locate(l, regex):
    for i,s in enumerate(l):
        for x in re.finditer(regex, s):
            yield i,x

def get_nums(l):
    d = {}
    for i,x in locate(l, r'\d+'):
        st,end = x.span()
        d[(i,st,end)] = int(x.group())
    return d

def get_symbols(l, regex):
    return set((i,x.start()) for i,x in locate(l, regex))

def generate(regex):
    l = str_list(3)
    symbols = get_symbols(l, regex)
    for c,n in get_nums(l).items():
        if t := is_valid(c,symbols):
            yield t,n

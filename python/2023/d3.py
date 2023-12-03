import re
from utils import str_list

def is_valid(c,symbols):
    line,(st, end) = c
    for row in range(line - 1, line + 2):
        for col in range(st - 1, end + 1):
            if (row,col) in symbols:
                return (row,col)
    return None

def locate(s, regex):
    return [x for x in re.finditer(regex, s)]

def get_nums(l):
    d = {}
    for i,s in enumerate(l):
        for x in locate(s, r'\d+'):
            v = x.span()
            d[(i,v)] = int(s[v[0]:v[1]])
    return d

def get_symbols(l, regex):
    st = set()
    for i,s in enumerate(l):
        for v in locate(s, regex):
            st.add(tuple([i,v.start()]))
    return st

def generate(regex):
    l = str_list(3)
    nums = get_nums(l)
    symbols = get_symbols(l, regex)
    return (nums, symbols)

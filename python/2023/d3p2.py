import re
from utils import str_list

def is_valid(c,symbols):
    line,(st, end) = c
    for row in range(line - 1, line + 2):
        for col in range(st - 1, end + 1):
            if (row,col) in symbols:
                return (row,col)
    return None

def get_nums(l):
    d = {}
    for i,s in enumerate(l):
        m = [x.span() for x in re.finditer(r'\d+', s)]
        for v in m:
            d[(i,v)] = int(s[v[0]:v[1]])
    return d

def get_symbols(l):
    st = set()
    for i,s in enumerate(l):
        m = [x.start() for x in re.finditer(r'[*]', s)]
        for v in m:
            st.add(tuple([i,v]))
    return st

def mul(vals):
    if len(vals) != 2:
        return 0
    return vals[0] * vals[1]

def solve(l):
    nums = get_nums(l)
    symbols = get_symbols(l)
    gears = {}
    for c,n in nums.items():
        t = is_valid(c,symbols)
        if t is not None:
            if t not in gears:
                gears[t] = []
            gears[t].append(n)
    return sum(map(mul, gears.values()))

print(solve(str_list(3)))

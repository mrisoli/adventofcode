import re
from utils import str_list

def is_valid(c,symbols):
    line,(st, end) = c
    for row in range(line - 1, line + 2):
        for col in range(st - 1, end + 1):
            if (row,col) in symbols:
                print(row,col)
                return True
    return False

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
        m = [x.start() for x in re.finditer(r'[^0-9.]', s)]
        for v in m:
            st.add(tuple([i,v]))
    return st

def solve(l):
    nums = get_nums(l)
    symbols = get_symbols(l)
    return sum([n for c,n in nums.items() if is_valid(c,symbols)])

print(solve(str_list(3)))

from utils import str_list
from d12 import parse_line,place

def expand(l):
    s,c = l
    s = '?'.join(5 * [s])
    c = 5 * c
    return s,c

print(sum([place(s,c) for s,c in map(expand, map(parse_line, str_list(12)))]))

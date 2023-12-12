from utils import str_list
from d12 import parse_line,place

print(sum([place(s,c) for s,c in map(parse_line,  str_list(12))]))

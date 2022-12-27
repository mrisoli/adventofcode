from math import prod
from d19 import calc,parse
from utils import str_list

print(prod(calc(b, 32) for _, *b in map(parse, str_list(19)[:3])))

from operator import mul
from functools import reduce
from utils import str_list
from d6 import ways, parse_num

def parse(l):
    d = [map(int, parse_num(c)) for c in l]
    return list(zip(d[0], d[1]))

print(reduce(mul, map(ways, parse(str_list(6)))))

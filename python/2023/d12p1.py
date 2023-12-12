import re
from itertools import combinations
from utils import str_list
from d12 import parse_line

def find(s):
    return [i for i, ltr in enumerate(s) if ltr == '?']

def place(s, c, o):
    ns = ['#' if i in o else c for i,c in enumerate(s)]
    ns = (''.join(ns)).replace('?', '.')
    return c == tuple(map(len, re.findall(r'#+', ns)))

def arrange(line):
    springs, count = parse_line(line)
    sp = springs.count('#')
    opens = find(springs)
    to_be_placed = sum(count) - sp
    return sum(map(lambda x: place(springs, count, x), combinations(opens, to_be_placed)))

print(sum(map(arrange,  str_list(12))))

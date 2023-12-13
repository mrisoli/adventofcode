import sys
import re

def get_path(n):
    t,v = 'i',''
    if len(sys.argv) > 1:
        t = 't'
        if sys.argv[1].isnumeric():
            v = '-' + sys.argv[1]
    return 'inputs/' + t + str(n) + v + '.in'

def int_list(n):
    return [*map(int, fopen(n))]

def int_row(n):
    return [*map(int, fopen(n).readline().split(','))]

def int_grid(n):
    return [[int(c) for c in l.strip()] for l in fopen(n).readlines()]

def rows_of_int(n):
    return [[*map(int, re.findall('-?\d+', l))] for l in fopen(n).readlines()]

def int_tuples(n):
    return {tuple(map(int, l.split(','))) for l in str_list(n)}

def get_cmd(s):
    (c, d) = s.split(' ')
    return (c, int(d))

def cmd_list(n):
    return [*map(get_cmd, fopen(n))]

def str_list(n):
    return [*map(str.strip, fopen(n))]

def fopen(n):
    return open(get_path(n))

def obj_list(n):
    return [*map(str.strip, fopen(n).read().split('\n\n'))]

def coords(n, tokens=None):
    if isinstance(n, int):
        n = str_list(n)
    return dict([(complex(i,j),x) for i,r in enumerate(n) for j,x in enumerate(r) if not tokens or x in tokens])

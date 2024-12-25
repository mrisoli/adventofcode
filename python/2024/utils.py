from functools import wraps
import sys
import re

def get_path(n):
    v = ''
    ext = '.in'
    if len(sys.argv) > 1:
        ext ='.test'
        if sys.argv[1].isnumeric():
            v = '-' + sys.argv[1]
    return 'inputs/' + 'day' + str(n) + v + ext

def int_list(n):
    return [*map(int, fopen(n))]

def int_row(n, separator=','):
    return [*map(int, fopen(n).readline().split(separator))]

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

def coords(n, tokens=None, parse=None, regex=None):
    if not parse:
        parse = lambda x: x
    if isinstance(n, int):
        n = str_list(n)
    return dict([(complex(i,j),parse(x)) for i,r in enumerate(n) for j,x in enumerate(r) if not tokens or x in tokens or (regex is not None and re.match(regex, x))])

def points_list(n):
    n = str_list(n)
    return [complex(v.replace(',','+')+'j') for v in n]


def hash_dict(func):
    """Transform mutable dictionnary
    Into immutable
    Useful to be compatible with cache
    """
    class HDict(dict):
        def __hash__(self):
            return hash(frozenset(self.items()))

    wraps(func)
    def wrapped(*args, **kwargs):
        args = tuple([HDict(arg) if isinstance(arg, dict) else arg for arg in args])
        kwargs = {k: HDict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapped

def det(a, b):
    return a.real * b.imag - a.imag * b.real

def polygon_area(p):
    area = abs(sum([det(a,b) for a,b in zip(p, p[1:] +[p[0]])]))
    return  int(((area - len(p))/2) + 1)

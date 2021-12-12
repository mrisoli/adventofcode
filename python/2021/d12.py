from utils import str_list

def link(m, v1, v2):
    if v1 not in m:
        m[v1] = set()
    if v1 != 'end' and v2 != 'start':
        m[v1].add(v2)

def build_map(s):
    m = {}
    for p in s:
        v1,v2 = p.split('-')
        link(m, v1, v2)
        link(m, v2, v1)
    return m

def is_small(s):
    return s.islower() and s not in ['start', 'end']

def solve(fn):
    print(fn(build_map(str_list(12)), 'start'))

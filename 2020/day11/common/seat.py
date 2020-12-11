from copy import deepcopy
import itertools

def count(m):
    return ''.join(itertools.chain(*m)).count('#')

def flip(l, i, j, o, n):
    # print(m[i][j], i, j, o)
    if l[i][j] == 'L' and o == 0:
        l[i][j] = '#'
    elif o >= n:
        l[i][j] = 'L'

def make_round(m, n, fn):
    l = deepcopy(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == '.':
                continue
            o = fn(m, i, j)
            flip(l, i, j, o, n)
    return l

def solve_with(n, fn):
    f = open('p.in')
    m = list(map(list, f.read().splitlines()))
    l = make_round(m, n, fn)
    while l != m:
        m = deepcopy(l)
        l = make_round(m, n, fn)
    print(count(m))

import re
from itertools import groupby
from utils import fopen

def cmds_and_stacks():
    p = [list(g) for k, g in groupby(fopen(5).readlines(), key=lambda x: x.startswith('move'))]
    diagram = [x for x in map(str.rstrip, p[0]) if x]
    cmds = [*map(lambda x: tuple(map(int, re.findall(r'\d+', x))), p[1])]
    stacks = [[] for i in range(int(diagram[-1][-1]) + 1)]
    bucket = dict([(i, int(v)) for i,v in enumerate(diagram[-1]) if v.isdigit()])
    for v in reversed(diagram[:-1]):
        [stacks[bucket[i]].append(c) for i,c in enumerate(v) if c.isalpha()]
    return (cmds, stacks)

def answer(stacks):
    print(''.join([s[-1] for s in stacks[1:]]))

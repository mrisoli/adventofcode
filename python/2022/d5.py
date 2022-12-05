import re
from utils import fopen

def cmds_and_stacks():
    diagram, cmds = [s.split('\n') for s in fopen(5).read().split('\n\n')]
    cmds = [tuple(map(int, re.findall(r'\d+', x))) for x in cmds if x]
    st = [[] for i in range(int(diagram[-1][-1]) + 1)]
    b = dict([(i, int(v)) for i,v in enumerate(diagram[-1]) if v.isdigit()])
    [[st[b[i]].append(c) for i,c in enumerate(v) if c.isalpha()] for v in reversed(diagram[:-1])]
    return (cmds, st)

def answer(s):
    print(''.join([x[-1] for x in s[1:]]))

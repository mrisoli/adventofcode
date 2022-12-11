import re
from itertools import zip_longest
from utils import obj_list

def cmds_and_stacks():
    d, cmds = [s.split('\n') for s in obj_list(5)]
    cmds = [tuple(map(int, re.findall(r'\d+', x))) for x in cmds if x]
    t = list(filter(lambda x: str(x[0]).isdigit(), map(list, zip_longest(*[*reversed(d)]))))
    st = [[]] + [[v for v in x[1:] if str(v or '').isalpha()] for x in t]
    return (cmds, st)

def answer(s):
    print(''.join([x[-1] for x in s[1:]]))

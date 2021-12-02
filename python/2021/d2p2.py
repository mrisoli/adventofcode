from utils import cmd_list
from functools import reduce

def move(p, cmd):
    (c, d) = cmd
    if c == 'forward':
        return (p[0] + d, p[1] + (d * p[2]), p[2])
    elif c == 'down':
        return (p[0], p[1], p[2] + d)
    else:
        return (p[0], p[1], p[2] - d)

p = reduce(move, cmd_list(2), (0,0,0))

print(p[0] * p[1])

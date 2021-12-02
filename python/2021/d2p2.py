from utils import cmd_list
from functools import reduce

def move(p, cmd):
    match cmd:
        case ('forward', d):
            return (p[0] + d, p[1] + (d * p[2]), p[2])
        case ('down', d):
            return (p[0], p[1], p[2] + d)
        case ('up', d):
            return (p[0], p[1], p[2] - d)

p = reduce(move, cmd_list(2), (0,0,0))

print(p[0] * p[1])

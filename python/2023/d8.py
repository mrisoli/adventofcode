from itertools import cycle
from utils import str_list

def node(data):
    name, dirs = map(str.strip, data.split('='))
    left,right = map(str.strip, dirs[1:-1].split(','))
    return (name, {'L':left, 'R':right})

def find(d, n, curr, destination):
    t = 0
    for s in cycle(d):
        t += 1
        curr = n[curr][s]
        if curr.endswith(destination):
            return t

def init():
    d,_, *m = str_list(8)
    return d,dict(map(node, m))

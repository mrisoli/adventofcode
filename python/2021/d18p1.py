from json import loads
from utils import fopen
from d18 import Tree

def run():
    f = fopen(18)
    l = f.readline()
    t = Tree(branches=loads(l))
    for l in f.readlines():
        s = Tree(branches=loads(l))
        t = t.combine_trees(s)
    print(t.magnitude())

run()

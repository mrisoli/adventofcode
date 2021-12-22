from json import loads
from utils import fopen
from d18 import Tree

def run():
    f = fopen(18)
    ll = f.readlines()
    m = 0
    for i in ll:
        for j in ll:
            if i != j:
                c = Tree(branches=loads(i))
                x = Tree(branches=loads(j))
                c = c.combine_trees(x)
                mm = c.magnitude()
                if mm > m:
                    m = mm
    print(m)
run()

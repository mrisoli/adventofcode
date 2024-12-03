import re
from math import prod

def solve(f):
    r = re.findall(r"mul\((\d+)\,(\d+)\)", f)
    print(sum(map(prod, (map(int, s) for s in r))))

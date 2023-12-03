import re
from utils import str_list
from d3 import generate, is_valid

def mul(vals):
    if len(vals) != 2:
        return 0
    return vals[0] * vals[1]

def solve():
    nums, symbols = generate(r'[*]')
    gears = {}
    for c,n in nums.items():
        t = is_valid(c,symbols)
        if t is not None:
            if t not in gears:
                gears[t] = []
            gears[t].append(n)
    return sum(map(mul, gears.values()))

print(solve())

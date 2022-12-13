from functools import cmp_to_key
from math import prod
from d13 import make, cmp

dividers = [[[2]], [[6]]]
l = [i for s in make() for i in s]
print(prod(i for i,v in enumerate(sorted(l + dividers, key=cmp_to_key(cmp)),1) if v in dividers))

from math import prod
from utils import str_list

def calc(l):
    *nums, op = l
    nums = map(int, nums)
    if op == '+':
        return sum(nums)
    return prod(nums)

f = list(zip(*[x.split() for x in str_list(6)]))
print(sum(map(calc, f)))

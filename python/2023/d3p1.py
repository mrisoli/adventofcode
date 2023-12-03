import re
from utils import str_list
from d3 import generate, is_valid

def solve():
    nums, symbols = generate(r'[^0-9.]')
    return sum([n for c,n in nums.items() if is_valid(c,symbols)])

print(solve())

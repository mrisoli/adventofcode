import re
from utils import str_list

number_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
}

def two_digits(r):
    print(sum([solve(x,r) for x in str_list(1)]))

def solve(l, r):
    m = re.findall(r, l)
    return int(parse(m[0]) + parse(m[-1]))

def parse(s):
    return number_mapping.get(s,s)

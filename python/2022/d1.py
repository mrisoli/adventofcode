from itertools import groupby
from utils import fopen

def get_list():
    l = fopen(1).read().split('\n')
    return list(sum([*map(int, g)]) for k,g in groupby(l, key=lambda x: x != '') if k)

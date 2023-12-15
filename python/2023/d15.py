from functools import reduce
from utils import fopen

def parse(x):
    return reduce(lambda acc,c:  ((acc + ord(c)) * 17) % 256, x, 0)

def make():
    return [*map(str.strip, fopen(15).readline().split(','))]

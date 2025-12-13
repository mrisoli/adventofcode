from utils import str_list
from functools import cache

def parse(s):
    key, value = s.split(": ")
    return key, value.split(" ")

G = dict(map(parse, str_list(11)))

@cache
def count(here, dest):
    return here == dest or sum(count(next, dest) for next in G[here])

print(count('you', 'out'))

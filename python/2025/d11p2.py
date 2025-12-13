from utils import str_list
from functools import cache

def parse(s):
    key, value = s.split(": ")
    return key, value.split(" ")

G = dict(map(parse, str_list(11)))

@cache
def count(here, dest):
    if here == dest:
        return 1
    if here not in G:
        return 0
    return sum(count(next, dest) for next in G[here])

fftdac = count('fft', 'dac')
ans = count('svr', 'fft') * fftdac * count('dac', 'out') if fftdac > 0 else count('svr', 'dac') * count('dac', 'fft') * count('fft', 'out')
print(ans)

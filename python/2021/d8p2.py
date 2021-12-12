from collections import Counter
from utils import fopen

default_pattern = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bdcf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def pattern_decoder(p):
    return Counter(''.join(p))

def translate(s, decoder):
    return tuple(sorted([decoder[x] for x in s]))

def calc(i, o):
    decoder = pattern_decoder(i)
    return int(''.join(map(str, [t[translate(x, decoder)] for x in o])))

def get_output(line):
    return calc(*[x.strip().split(' ') for x in line])

t = {}
default_count = pattern_decoder(default_pattern)
for i, x in enumerate(default_pattern):
    k = translate(x, default_count)
    t[k] = i

print(sum([get_output(e.split('|')) for e in fopen(8).readlines()]))

from functools import reduce
from operator import mul
from utils import str_list

def power_cubes(data):
    mins = { 'blue': 0, 'red': 0, 'green':  0}
    for game in data.split(';'):
        for d in game.strip(' ').split(', '):
            n, c = d.split(' ')
            mins[c] = max(mins[c], int(n))
    return reduce(mul, mins.values())

def get_data(g):
    return g.split(':')

def games(l):
    return sum([power_cubes(data) for _, data in map(get_data, l)])

print(games(str_list(2)))

from functools import reduce
from operator import mul
from utils import str_list

def power_cubes(data):
    sets = data.split(';')
    mins = { 'blue': 0, 'red': 0, 'green':  0}
    for game in sets:
        dt = game.strip(' ').split(', ')
        for d in dt:
            n, c = d.split(' ')
            mins[c] = max(mins[c], int(n))
    return reduce(mul, mins.values())

def get_data(g):
    return g.split(':')

def games(l):
    return sum([power_cubes(data) for _, data in map(get_data, l)])


l = str_list(2)
print(games(l))

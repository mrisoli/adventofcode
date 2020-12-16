from functools import reduce
from common import slope

f = open('puzzle.in', 'r').read().splitlines()
print(reduce(lambda x,y: x * slope.run(f, y, 1), range(1, 8, 2), 1) * slope.run(f, 1, 2))

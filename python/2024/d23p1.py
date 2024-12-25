from itertools import combinations
from utils import str_list

f = str_list(23)
computers, connections = set(), set()
for line in f:
    a,b = line.split('-')
    computers.update([a,b])
    connections.update([(a,b), (b,a)])

print(sum({(a,b), (b,c), (c,a)} < connections
          and 't' in (a + b + c)[::2]
          for a, b, c in combinations(computers, 3)))

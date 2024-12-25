from itertools import combinations
from utils import str_list

f = str_list(23)
computers, connections = set(), set()
for line in f:
    a,b = line.split('-')
    computers.update([a,b])
    connections.update([(a,b), (b,a)])

networks = [{c} for c in computers]
for n in networks:
    for c in computers:
        if all((c,d) in connections for d in n): n.add(c)

print(*sorted(max(networks, key=len)), sep=',')

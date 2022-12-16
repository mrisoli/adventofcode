from dataclasses import dataclass, field
from utils import str_list

@dataclass
class Valve:
    rate: int
    tunnels: list[str]

def open_valve(t, v):
    if v in op:
        return 0
    else:
        op.add(v)
        tv = (t - 1) * valves[v].rate
        return tv

def run(t, v):
    if t == 0:
        return 0
    o = open_valve(t, v)
    mv = [*map(lambda u: run(t - 1, u), valves[v].tunnels)]
    m = [o + run(t - 1, v), *mv]
    return max(m)

f = str_list(16)
valves = {}
op = set()
for l in f:
    rate,tu = l.split(';')
    va,rate = rate.split('=')
    va = va[6:8]
    tu = [*map(lambda x: x.strip(','), tu.split(' ')[5:])]
    valves[va] = Valve(rate=int(rate),tunnels=tu)
print(run(30, 'AA'))

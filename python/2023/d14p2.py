from collections import Counter
from d14 import calc,lever,make,rotate

def cycle(f):
    for _ in range(4):
        f = rotate(lever(f))
    return f

def run(f):
    states = [f]
    period = transient = t = 0
    target = 1_000_000_000
    while True:
        end_cycle = cycle(states[t])
        if end_cycle in states:
            transient = states.index(end_cycle)
            period = t + 1 - states.index(end_cycle)
            break
        states.append(end_cycle)
        t += 1
    return states[(target - transient) % period + transient]

print(calc(run(make())))

from functools import reduce
import heapq

def calc(l):
    s = list(map(int, l.split('x')))
    h = heapq.nsmallest(2, s)
    return (2 * h[0]) + (2 * h[1]) + reduce(lambda x, y: x * y, s, 1)

with open('puzzle.in', 'r') as f:
    print(reduce(lambda x, y: x + calc(y), f.read().splitlines(), 0))

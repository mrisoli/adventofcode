from functools import reduce

def calc(l):
    s = list(map(int, l.split('x')))
    [w, l, h] = s
    lw = l * w
    lh = l * h
    hw = h * w
    return (2 * lw) + (2 * lh) + (2 * hw)  + min([lw, lh, hw])

with open('puzzle.in', 'r') as f:
    print(reduce(lambda x, y: x + calc(y), f.read().splitlines(), 0))

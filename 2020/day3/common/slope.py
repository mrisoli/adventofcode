from functools import reduce
def run(f, d, v):
    h,s = 0,0
    for n in range(0,len(f), v):
        if f[n][h] == '#':
            s += 1
        h = (h + d) % len(f[n])
    return s

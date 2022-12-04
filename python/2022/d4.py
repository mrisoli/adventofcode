from utils import str_list

def rn(v):
    return range(v[0],v[1] + 1)

def get_ranges(r):
    r1 = rn(r[0])
    r2 = rn(r[1])
    return (len(set(r1).intersection(r2)), len(r1), len(r2))

def overlap(pred):
    l = [[[int(v) for v in r.split('-')] for r in s.split(',')] for s in str_list(4)]
    return len(list(filter(pred, map(get_ranges, l))))

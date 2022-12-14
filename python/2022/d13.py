from utils import obj_list

def make():
    return [[eval(p) for p in v] for v in map(str.split, obj_list(13))]

def cmp(l, r):
    match l, r:
        case int(), int(): return l - r
        case list(), int(): r = [r]
        case int(), list(): l = [l]
    return next((c for c in map(cmp, l, r) if c), len(l) - len(r))

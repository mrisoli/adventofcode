from utils import str_list

def can_pop(s, c):
    return (s + c) in ['<>', '[]', '()', '{}']

def calc(l, vs):
    t = 0
    for c in l[::-1]:
        t *= 5
        t += vs[c]
    return t

def points(l, fix, vs):
    s = []
    for c in l:
        if c in '<[({':
            s.append(c)
        elif can_pop(s[-1], c):
            s.pop()
        else:
            return 0 if fix else vs[c]
    return calc(s, vs) if fix else 0

def get_values(fix, vs):
    return [points(l, fix, vs) for l in str_list(10)]

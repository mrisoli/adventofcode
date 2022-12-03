def val(s):
    if ord(s) >= 97:
        return ord(s) - 96
    else:
        return ord(s) - 38

def priority(v):
    s = list(set.intersection(*map(set,v)))
    return val(s[0])

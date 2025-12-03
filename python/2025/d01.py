from utils import str_list

def parse(c):
    d, v = c[0], c[1:]
    return (d, int(v))

def make():
    return map(parse, str_list(1))

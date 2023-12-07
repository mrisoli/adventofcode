import re

def parse_num(v):
    return re.findall('\d+', v.split(':')[1])

def ways(w):
    t, d = w
    return len(list(filter(lambda i: i * (t - i) > d, range(1, t))))

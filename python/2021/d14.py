from math import ceil
from utils import str_list
from collections import Counter

def get_rule(s):
    (c, d) = s.split('->')
    return (c.strip(), d.strip())

def parse_rules(r):
    return {k:v for k,v in [*map(get_rule, r)]}

def run(s, r):
    cc = Counter()
    for el,t in s.items():
        st = el[0] + r[el]
        ts = r[el] + el[1]
        cc[st] += t
        cc[ts] += t
    return cc

def count(sc, start, end):
    c = Counter()
    for p,q in sc.items():
        c[p[0]] += q
        c[p[1]] += q
    c[start] += 1
    c[end] += 1
    mc = c.most_common()
    print(ceil((mc[0][1] - mc[-1][1]) / 2))

def solve(n):
    s, _, *rules = str_list(14)
    rules = parse_rules(rules)
    sc = Counter(map(lambda x: ''.join(x), zip(s, s[1:])))
    for _ in range(n):
        sc = run(sc, rules)

    count(sc, s[0], s[1])

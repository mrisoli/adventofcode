from math import prod
import re
re_fields = re.compile(r'(.+):\s(\d+-\d+)\sor\s(\d+-\d+)')
f = open('p.in')
[fields, tickets] = f.read().split('your ticket:\n')
fs = {}
s = set()
fis = [x for x in fields.split('\n') if x]
for fi in fis:
    [field, r1, r2] = re.match(re_fields, fi).groups()
    fs[field] =  set()
    for r in [r1,r2]:
        [mn,mx] = list(map(int, r.split('-')))
        rn = set(range(mn, mx +1))
        s = s.union(rn)
        fs[field] = fs[field].union(rn)
[your_ticket, nearby] = tickets.rstrip().split('nearby tickets:\n')
your_ticket = your_ticket.rstrip()
nearby = [list(map(int, ticket.split(','))) for ticket in nearby.split('\n')]
valid_tickets = [ticket for ticket in nearby if all(map(lambda x: x in s, ticket))]
cols = list(zip(*valid_tickets))

sols = {}
for field,solutions in fs.items():
    sols[field] = []
    for ci in range(len(cols)):
        if all(i in solutions for i in cols[ci]):
            sols[field].append(ci)
sols = list(sols.items())
sols.sort(key=lambda x: len(x[1]))
taken = set()
lis = {}
for (k,v) in sols:
    if len(v) == 1:
        lis[k] = v[0]
        taken.add(v[0])
    else:
        diff = list(set(v) - taken)[0]
        lis[k] = diff
        taken.add(diff)

your_ticket = list(map(int, your_ticket.split(',')))
print(prod([your_ticket[v] for k, v in lis.items() if k.startswith('departure')]))

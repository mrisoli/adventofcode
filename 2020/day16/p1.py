import re
re_fields = re.compile(r'(\w+\s?)+:\s(\d+-\d+)\sor\s(\d+-\d+)')
f = open('p.in')
[fields, tickets] = f.read().split('your ticket:\n')
s = set()
for fi in [x for x in fields.split('\n') if x]:
    [field, r1, r2] = re.match(re_fields, fi).groups()
    for r in [r1,r2]:
        [mn,mx] = list(map(int, r.split('-')))
        rn = set(range(mn, mx +1))
        s = s.union(rn)
[your_ticket, nearby] = tickets.rstrip().split('nearby tickets:\n')
your_ticket = your_ticket.rstrip()
all_tickets = [your_ticket] + nearby.split('\n')
invalids = []
for ticket in all_tickets:
    invalids += list(filter(lambda x: x not in s, map(int, ticket.split(','))))
print(sum(invalids))

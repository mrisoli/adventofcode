import re
f = open('p.in').readlines()
messages = [x.strip() for x in f if x[0] in 'ab']
rr = [x.strip() for x in f if x[0].isdigit()]
rules = {}
for r in rr:
    [i, rule] = r.split(':')
    rules[int(i)] = rule.strip().strip('"')
rule = ' ' + rules[0] + ' '
while any(i.isdigit() for i in rule):
    numbers = [int(s) for s in rule.split() if s.isdigit()]
    for n in numbers:
        nrule = '( ' + rules[n] + ' )' if '|' in rules[n] else rules[n]
        rule = rule.replace(' '+ str(n) + ' ', ' ' + nrule + ' ')
rule = re.compile('^' + rule.replace(' ', '') + '$')
print(sum([1 for m in messages if rule.match(m)]))

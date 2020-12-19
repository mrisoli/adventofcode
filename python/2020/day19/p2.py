import re
f = open('p.in').readlines()
rr = [x.strip() for x in f if x[0].isdigit()]
messages = [x.strip() for x in f if x[0] in 'ab']
rules = {}
for r in rr:
    [i, rule] = r.split(':')
    rules[int(i)] = rule.strip().strip('"')
rules[0] = ' 42 + 42 {n} 31 {n}'
rule = ' ' + rules[0] + ' '
while any(i.isdigit() for i in rule):
    numbers = [int(s) for s in rule.split() if s.isdigit()]
    for n in numbers:
        nrule = '( ' + rules[n] + ' )' if '|' in rules[n] else rules[n]
        rule = rule.replace(' '+ str(n) + ' ', ' ' + nrule + ' ')
rule = '^' + rule.replace(' ', '') + '$'
sols = []
for i in range(1,5):
    rulecp = rule
    rulecp = rulecp.replace('n', str(i))
    rulecp = re.compile(rulecp)
    s = (sum([1 for m in messages if rulecp.match(m)]))
    sols.append(s)
print(sum(sols))

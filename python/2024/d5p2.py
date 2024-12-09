from d5 import RuleChecker

r = RuleChecker()
print(sum([r.value(r.fix(u)) for u in r.update if not r.check(u)]))

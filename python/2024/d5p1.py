from d5 import RuleChecker
r = RuleChecker()
print(sum([r.value(u) for u in r.update if r.check(u)]))

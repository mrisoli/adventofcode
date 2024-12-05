from utils import obj_list

class RuleChecker:
    def __init__(self):
        [rules, update] = obj_list(5)
        rules = self.parse_rules(rules)
        self.rules = rules
        self.update = [*map(self.parse_update, update.split('\n'))]

    def parse_update(self, u):
        return [*map(int, u.split(','))]

    def parse_rules(self, r):
        s = {}
        for x in r.split('\n'):
            [k, v] = [int(n) for n in x.split('|')]
            if k not in s:
                s[k] = []
            s[k].append(v)
        return s

    def value(self, u):
        return u[len(u) // 2]

    def check(self, u):
        head, *tail = u
        if len(tail) == 0:
            return True
        for t in tail:
            if head in self.rules.get(t, []) and t not in self.rules.get(head, []):
                return False
        return self.check(tail)

    def fix(self, a):
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] in self.rules.get(a[j], []):
                    a[i], a[j] = a[j], a[i]
        return a

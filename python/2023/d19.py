from typing import NamedTuple

def get_rules(rs: str) -> dict[str, [str]]:
    rules = {}
    for r in rs.split('\n'):
        n, d = r[:-1].split('{')
        rules[n] = d.split(',')
    return rules

def apply_less(r: range, value: int):
    if r.start > value:
        return range(0), r
    if r.stop > value:
        return range(r.start, value), range(value, r.stop)
    return r, range(0)


def apply_more(r: range, value: int):
    if r.stop < value:
        return range(0), r
    if r.start <= value:
        return range(value + 1, r.stop), range(r.start, value + 1)
    return r, range(0)

class Parts(NamedTuple):
    x: range
    m: range
    a: range
    s: range

    @property
    def size(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)

    def _apply(self, func, name: str, value: int):
        a, b = self._asdict(), self._asdict()
        a[name], b[name] = func(a[name], value)
        return Parts(**a), Parts(**b)

    def apply_less(self, name: str, value: int):
        return self._apply(apply_less, name, value)

    def apply_more(self, name: str, value: int):
        return self._apply(apply_more, name, value)

class Solver:
    def __init__(self, rules: dict[str, str]):
        self.rules = get_rules(rules)

    def solve(self, part: Parts, name: str) -> int:
        if part.size == 0:
            return 0
        if name == 'A':
            return part.size
        if name == 'R':
            return 0
        result = 0
        for rule in self.rules[name]:
            if ':' in rule:
                cond, target = rule.split(':')
                if '>' in cond:
                    name, value = cond.split('>')
                    a, part = part.apply_more(name, int(value))
                    result += self.solve(a, target)
                elif '<' in cond:
                    name, value = cond.split('<')
                    a, part = part.apply_less(name, int(value))
                    result += self.solve(a, target)
                else:
                    assert 0, rule
            else:
                result += self.solve(part, rule)
        return result

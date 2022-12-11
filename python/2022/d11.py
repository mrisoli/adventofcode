import re
from math import prod
from operator import mul
from dataclasses import dataclass
from heapq import nlargest
from utils import obj_list

total = None

@dataclass
class Monkey:
    items: list[int]
    op: str
    test: int
    truthy: int
    falsy: int
    business: int = 0

    def inspect(self, old):
        self.business += 1
        return eval(self.op)

    def inspection(self, n):
        for v in self.items:
            v = (self.inspect(v) // n) % total
            if v % self.test == 0:
                yield (self.truthy, v)
            else:
                yield (self.falsy, v)
        self.items.clear()

@dataclass
class MonkeyList:
    monkeys: list[Monkey]
    n: int

    def round(self):
        for m in self.monkeys:
            for (target, v) in m.inspection(self.n):
                self.monkeys[target].items.append(v)

def make_monkey(o):
    _, items, op, *tests = o.split('\n')[:6]
    items = list(map(int, re.findall(r'\d+', items)))
    op = op.split('=')[1]
    [test, truthy, falsy] = [int(re.search(r'\d+', x).group(0)) for x in tests]
    return Monkey(items=items, op=op, test=test, truthy=truthy, falsy=falsy)

def get_monkeys():
    global total
    monkeys = [make_monkey(o) for o in obj_list(11)]
    total = prod(map(lambda m: m.test, monkeys))
    return monkeys

def rounds(r, n):
    monkeys = get_monkeys()
    for i in range(r):
        for m in monkeys:
            for (target, v) in m.inspection(n):
                monkeys[target].items.append(v)

    print(mul(*nlargest(2, map(lambda m: m.business, monkeys))))

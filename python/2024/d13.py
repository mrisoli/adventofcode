import re
from utils import obj_list

COST = [3,1]
def parse(v):
    r = list(map(int, re.findall(r'\d+', v)))
    return r[0] + r[1] * 1j

class Machine:
    def __init__(self, s, enlarge=False):
        [a, b, p] = s.split('\n')
        self.a = parse(a)
        self.b = parse(b)
        self.prize = parse(p)
        self.enlarge = enlarge
        if enlarge:
            self.prize += 10000000000000 + 10000000000000j

    def solve(self):
        d = self.a.real * self.b.imag - self.a.imag * self.b.real
        a = int((self.prize.real * self.b.imag - self.prize.imag * self.b.real) // d)
        b = int((self.a.real * self.prize.imag - self.a.imag * self.prize.real) // d)
        if self.a.real * a + self.b.real * b == self.prize.real and self.a.imag * a + self.b.imag * b == self.prize.imag:
            return a * 3 + b
        return 0

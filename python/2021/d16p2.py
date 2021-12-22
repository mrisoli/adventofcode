from utils import fopen
from operator import mul
from functools import reduce

class Parser(object):
    def __init__(self, bits):
        self.bits = bits
        self.i = 0
        self.versions = 0

    def read(self, n):
        v = 0
        for _ in range(n):
            v <<= 1
            if self.i < len(self.bits):
                if self.bits[self.i] == '1':
                    v |= 1
                self.i += 1
        return v

    def parse(self):
        version = self.read(3)
        t = self.read(3)
        self.versions += version
        if t == 4:
            return self.parse_literal()
        elif t == 0:
            op = sum
        elif t == 1:
            op = lambda v: reduce(mul, v, 1)
        elif t == 2:
            op = min
        elif t == 3:
            op = max
        elif t == 5:
            op = lambda v: 1 if v[0] > v[1] else 0
        elif t == 6:
            op = lambda v: 1 if v[0] < v[1] else 0
        elif t == 7:
            op = lambda v: 1 if v[0] == v[1] else 0
        return self.parse_operator(op)

    def parse_operator(self, op):
        if self.read(1) == 0:
            return self.parse_l_operator(op, self.read(15))
        else:
            return self.parse_n_operator(op, self.read(11))

    def parse_literal(self):
        v = 0
        while True:
            b = self.read(1)
            d = self.read(4)
            v = (v << 4) | d
            if b == 0:
                return v

    def parse_l_operator(self, op, length):
        j = self.i + length
        v = []
        while self.i < j:
            v.append(self.parse())
        return op(v)


    def parse_n_operator(self, op, num):
        return op([self.parse() for _ in range(num)])

def solve(f=None):
    s = f if f else fopen(16).readline().strip()
    b = bin(int(s, 16))[2:]
    b = b.zfill(len(s) * 4)
    p = Parser(b)
    v = p.parse()
    return v

if __name__ == '__main__':
    print(solve())

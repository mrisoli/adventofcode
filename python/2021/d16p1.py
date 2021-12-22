from utils import fopen

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
            self.parse_literal()
        else:
            self.parse_operator()

    def parse_operator(self):
        if self.read(1) == 0:
            return self.parse_l_operator(self.read(15))
        else:
            return self.parse_n_operator(self.read(11))

    def parse_literal(self):
        v = 0
        while True:
            b = self.read(1)
            self.read(4)
            if b == 0:
                return v

    def parse_l_operator(self, length):
        j = self.i + length
        while self.i < j:
            self.parse()

    def parse_n_operator(self, num):
        [self.parse() for _ in range(num)]

def solve(f=None):
    s = f if f else fopen(16).readline().strip()
    b = bin(int(s, 16))[2:]
    b = b.zfill(len(s) * 4)
    p = Parser(b)
    p.parse()
    print(p.versions)
    return p.versions

if __name__ == '__main__':
    solve()

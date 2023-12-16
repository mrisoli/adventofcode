from utils import str_list, coords

class Grid:
    def __init__(self):
        s = str_list(16)
        self.z = coords(s, '/\|-')
        self.mr = len(s[0])
        self.mc = len(s)

    def move_beam(self, b):
        d,p = b
        beams = []
        while p.real in range(self.mr) and p.imag in range(self.mc):
            self.energized.add(tuple([d,p]))
            if p in self.z:
                if self.z[p] == '/':
                    d = -d.imag - (1j * d.real)
                elif self.z[p] == '\\':
                    d = d.imag + (1j * d.real)
                elif self.z[p] == '|' and d.real == 0:
                    d = 1
                    beams += [(-1, p)]
                elif self.z[p] == '-' and d.imag == 0:
                    d = 1j
                    beams += [(-1j, p)]
            p += d
        return beams

    def run(self, beams):
        v = set()
        self.energized = set()
        while beams:
            b = beams.pop(0)
            v.add(b)
            if b not in self.energized:
                nb = self.move_beam(b)
                beams += [b for b in nb if b not in v]
        return len(set(p for _,p in self.energized))

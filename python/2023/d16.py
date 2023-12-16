from utils import str_list, coords

class Grid:
    def __init__(self, beams):
        s = str_list(16)
        self.z = coords(s, '/\|-')
        self.mr = len(s[0])
        self.mc = len(s)
        self.energized = set()
        self.beams = beams

    def move_beam(self, b):
        d,p = b
        beams = []
        while p.real in range(self.mr) and p.imag in range(self.mc):
            if (d,p) in self.energized:
                return beams
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

    def set_beams(self, beams):
        self.beams = beams
        return self

    def run(self):
        v = set()
        self.energized = set()
        while self.beams:
            b = self.beams.pop(0)
            v.add(b)
            new_beams = self.move_beam(b)
            self.beams += [b for b in new_beams if b not in v]
        self.energized = set(p for _,p in self.energized)
        return len(self.energized)

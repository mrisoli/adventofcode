from utils import str_list

class Solver:
    def __init__(self):
        self.data = {}
        s = str_list(20)
        self.conj_memory = {}
        for x in s:
            a, b = x.split(' -> ')
            self.data[a] = b.split(', ')
            if a.startswith('&'):
                self.conj_memory[a] = {}

        self.flip_flop_states = {k: False for k in self.data.keys() if k.startswith('%')}
        for c in self.conj_memory.keys():
            for k,v in self.data.items():
                if c[1:] in v:
                    self.conj_memory[c][k] = False
        self.pulse_counts = {'low': 0, 'high': 0}

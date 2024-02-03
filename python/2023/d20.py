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

    def handle_flip_flop(self, module, pulse):
        if pulse == 'low':
            self.flip_flop_states[module] = not self.flip_flop_states[module]
            return 'high' if self.flip_flop_states[module] else 'low'
        return None

    def handle_conjunction(self, module, source, pulse):
        self.conj_memory[module][source] = (pulse == 'high')
        if all(self.conj_memory[module].values()):
            return 'low'
        return 'high'

    def transmit_pulse(self, module, pulse, source):
        m = '%' + module
        if m in self.data:
            return m, self.handle_flip_flop(m, pulse)
        m = '&' + module
        if m in self.data:
            return m, self.handle_conjunction(m, source, pulse)
        return module, pulse

    def solve(self):
        queue = [('broadcaster', 'low', 'button')]
        while queue:
            current_module, current_pulse, source = queue.pop(0)
            if current_pulse:
                self.pulse_counts[current_pulse] += 1
                current_module, new_pulse = self.transmit_pulse(current_module, current_pulse, source)
                if current_module in self.data:
                    for next_module in self.data[current_module]:
                        queue.append((next_module, new_pulse, current_module))


    def count(self):
        return self.pulse_counts['low'] * self.pulse_counts['high']

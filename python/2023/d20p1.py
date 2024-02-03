from d20 import Solver

def handle_flip_flop(s, module, pulse):
    if pulse == 'low':
        s.flip_flop_states[module] = not s.flip_flop_states[module]
        return 'high' if s.flip_flop_states[module] else 'low'
    return None

def handle_conjunction(s, module, source, pulse):
    s.conj_memory[module][source] = (pulse == 'high')
    if all(s.conj_memory[module].values()):
        return 'low'
    return 'high'

# Function to transmit pulse
def transmit_pulse(s, module, pulse, source):
    m = '%' + module
    if m in s.data:
        return m, handle_flip_flop(s, m, pulse)
    m = '&' + module
    if m in s.data:
        return m, handle_conjunction(s, m, source, pulse)
    return module, pulse

def solve(s):
    for _ in range(1000):
        # Broadcast pulse to all connected modules
        queue = [('broadcaster', 'low', 'button')]
        while queue:
            current_module, current_pulse, source = queue.pop(0)
            if current_pulse:
                s.pulse_counts[current_pulse] += 1
                current_module, new_pulse = transmit_pulse(s, current_module, current_pulse, source)
                if current_module in s.data:
                    for next_module in s.data[current_module]:
                        queue.append((next_module, new_pulse, current_module))
    return s.pulse_counts['low'] * s.pulse_counts['high']

result = Solver()
print(solve(result))

from collections import defaultdict
from functools import cache
from itertools import combinations
from utils import str_list

def make_button(button):
    button = button[1:-1]
    if button:
        return tuple(int(i) for i in button.split(','))

def make_buttons(buttons):
    return list(map(make_button, buttons))

def powerset(s):
    for r in range(len(s)+1): yield from combinations(s,r)

def solve(data):
    # We ignore the first element (formerly 'lights') using '_'
    _, *buttons, demands = data.split(' ')
    buttons = make_buttons(buttons)
    demands = tuple(map(int, demands[1:-1].split(',')))

    options, output = defaultdict(list), dict()

    # Precompute button subsets and their effects
    for pressed in powerset(range(len(buttons))):
        supply = [len([1 for b in pressed if j in buttons[b]])
                         for j in range(len(demands))]
        parity = tuple(j%2 for j in supply)

        options[parity] += [pressed]
        output[pressed] = supply

    @cache
    def opt(demands):
        if min(demands)  < 0: return 1e99
        if sum(demands) == 0: return 0

        answer = 1e99
        parity = tuple(j%2 for j in demands)

        for pressed in options[parity]:
            remain = tuple((j-s)//2 for j,s in zip(demands, output[pressed]))
            answer = min(answer, len(pressed) + 2*opt(remain))

        return answer

    # Only return the result for Part 2 (Integer Targets)
    return opt(demands)

print(sum(map(solve, str_list(10))))

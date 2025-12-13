from collections import deque
from utils import fopen

def make_button(button):
    button = button[1:-1]
    if button:
        return tuple(int(i) for i in button.split(','))
    else:
        return ()
def make_buttons(buttons):
    return list(map(make_button, buttons))

def run(lights, buttons):
    queue = deque()
    seen = set()
    queue.append((lights, 0))
    while queue:
        current_lights, presses = queue.popleft()
        if not current_lights:
            return presses
        for button in buttons:
            new_lights = current_lights.copy()
            for b in button:
                if b in new_lights:
                    new_lights.remove(b)
                else:
                    new_lights.add(b)
            new_lights_frozenset = frozenset(new_lights)
            if new_lights_frozenset not in seen:
                seen.add(new_lights_frozenset)
                queue.append((new_lights, presses + 1))

def solve(data):
    lights, *buttons, _ = data.split(' ')
    buttons = make_buttons(buttons)
    lights = set(i for i, c in enumerate(lights[1:-1]) if c == '#')
    return run(lights, buttons)

print(sum(map(solve, fopen(10).readlines())))

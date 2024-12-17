from utils import obj_list

MOVE = {'^': -1, 'v': 1, '<': -1j, '>': 1j}

def calc():
    return sum(int(abs(100 * k.real)) + int(abs(k.imag)) for k,v in diagram.items() if v == 'O')

def move_box(box, move):
    rng = box + move
    points = [box]
    while diagram.get(rng) == 'O':
        points.append(rng)
        rng += move
    if diagram.get(rng) == '#':
        return False
    points.append(rng)
    for p in points:
        diagram[p] = 'O'
    return True

def move(robot, move):
    if diagram.get(robot + move) == '.':
        diagram[robot + move] = '@'
        diagram[robot] = '.'
        return robot + move
    elif diagram.get(robot + move) == '#':
        return robot
    elif diagram.get(robot + move) == 'O':
        box = robot + move
        if diagram.get(box + move) == '.':
            diagram[box + move] = 'O'
            diagram[box] = '@'
            diagram[robot] = '.'
            return box
        elif diagram.get(box + move) == 'O':
            if move_box(box, move):
                diagram[box] = '@'
                diagram[robot] = '.'
                return box
    return robot

def pprint():
    t = [k for k,v in diagram.items() if v == 'O']
    print(robot, t)

[diagram, seq] = obj_list(15)
seq = [d for d in seq if d in MOVE.keys()]
diagram = diagram.split('\n')
diagram = {(r + c * 1j):col for r, row in enumerate(diagram) for c,col in enumerate(row)}
robot = next(k for k,v in diagram.items() if v == '@')
for d in seq:
    robot = move(robot, MOVE[d])
print(calc())

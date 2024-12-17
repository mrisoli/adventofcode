from utils import obj_list

MOVE = {'^': -1, 'v': 1, '<': -1j, '>': 1j}

def get_edge(v, d):
    return int(v if v < d - v + 1 else v + 1)

def is_box(p):
    return diagram.get(p) == '[' or diagram.get(p) == ']'

def get_boxes(p):
    if diagram.get(p) == '[':
        return [p, p + 1j]
    return [p - 1j, p]

def calc():
    return sum(int(100 * k.real) + int(k.imag) for k,v in diagram.items() if v == '[')

def move_box(box, move):    
    [left_edge, right_edge] = get_boxes(box)
    boxes_to_check = [left_edge, right_edge]
    current = 0
    
    while current < len(boxes_to_check):
        current_box = boxes_to_check[current]
        next_pos = current_box + move
        if diagram.get(next_pos) == '#':
            return False
        if next_pos not in boxes_to_check and is_box(next_pos):
            boxes_to_check += get_boxes(next_pos)
        current += 1
    
    new_pos = {p + move:diagram[p] for p in boxes_to_check}
    clear = {p:'.' for p in boxes_to_check if p not in new_pos}
    diagram.update(new_pos)
    diagram.update(clear)
    
    return True

def move_robot(robot, move):
    next_pos = robot + move
    if diagram.get(next_pos) == '.':
        diagram[next_pos] = '@'
        diagram[robot] = '.'
        return next_pos
    elif is_box(next_pos):
        if move_box(next_pos, move):
            diagram[next_pos] = '@'
            diagram[robot] = '.'
            return next_pos
    return robot

def expand(d):
    e = ""
    for v in d:
        if v == '#':
            e += '##'
        elif v == '.':
            e += '..'
        elif v == '@':
            e += '@.'
        elif v == 'O':
            e += '[]'
        else:
            e += v
    return e

def pprint(d):
    mx = max(map(lambda x: int(x.real), d.keys()))
    my = max(map(lambda x: int(x.imag), d.keys()))
    for i in range(mx + 1):
        for j in range(my + 1):
            print(d[i + (1j * j)], end='')
        print('')

[diagram, seq] = obj_list(15)
seq = [d for d in seq if d in MOVE.keys()]
diagram = expand(diagram)
diagram = diagram.split('\n')
mx = len(diagram)
my = len(diagram[0])
diagram = {(r + c * 1j):col for r, row in enumerate(diagram) for c,col in enumerate(row)}
robot = next(k for k,v in diagram.items() if v == '@')
for d in seq:
    robot = move_robot(robot, MOVE[d])
print(calc())

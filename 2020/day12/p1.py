dirs = 'NESW'

def change_dir(c, d):
    curr = dirs.find(c['dir'])
    c['dir'] = dirs[(curr + (d // 90)) % 4]

def make_move(c, m):
    direction,distance = m
    if direction in 'NS':
        c['ns'] += distance if direction == 'N' else - distance
    elif direction in 'EW':
        c['ew'] += distance if direction == 'E' else - distance
    elif direction == 'F':
        make_move(c, [c['dir'], distance])
    elif direction in 'LR':
        change_dir(c, distance if direction == 'R' else - distance)

f = open('p.in')
moves = [[x[0], int(x[1:])] for x in f.read().splitlines()]
coord = {'ew': 0, 'ns': 0, 'dir': 'E'}
for m in moves:
    make_move(coord, m)
print(abs(coord['ew']) + abs(coord['ns']))

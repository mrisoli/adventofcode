def change_dir(w, d):
    if abs(d) == 180:
        w['ns'],w['ew'] = -w['ns'],-w['ew']
    elif d == 90 or d == -270:
        w['ns'],w['ew'] = -w['ew'],w['ns']
    else:
        w['ns'],w['ew'] = w['ew'],-w['ns']

def make_move(c, w, m):
    dirs,dist = m
    if dirs in 'NS':
        w['ns'] += dist if dirs == 'N' else - dist
    elif dirs in 'EW':
        w['ew'] += dist if dirs == 'E' else - dist
    elif dirs == 'F':
        c['ew'] += w['ew'] * dist
        c['ns'] += w['ns'] * dist
    elif dirs in 'LR':
        change_dir(w, dist if dirs == 'R' else - dist)

f = open('p.in')
moves = [[x[0], int(x[1:])] for x in f.read().splitlines()]
coord = {'ew': 0, 'ns': 0}
waypoint = {'ew': 10, 'ns': 1}
for m in moves:
    make_move(coord, waypoint, m)
print(abs(coord['ew']) + abs(coord['ns']))

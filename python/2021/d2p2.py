from utils import cmd_list

l = cmd_list(2)

def move(p, c, d):
    if c == 'forward':
        return (p[0] + d, p[1] + (d * p[2]), p[2])
    elif c  == 'down':
        return (p[0], p[1], p[2] + d)
    else:
        return (p[0], p[1], p[2] - d)

p = (0, 0, 0)

for (c, d) in l:
    p = move(p, c, d)

print(p[0] * p[1])

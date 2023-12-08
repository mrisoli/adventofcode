from d8 import init

d,nodes = init()
c = 'AAA'
t = 0
s = 0
while c != 'ZZZ':
    t += 1
    dr = d[s]
    s = (s + 1) % len(d)
    if dr == 'L':
        c = nodes[c].left
    elif dr == 'R':
        c = nodes[c].right
print(t)

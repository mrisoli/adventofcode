from utils import str_list

f = str_list(10)

x,t,i = 1,0,None
for c in range(1,221):
    if not i:
        l = f.pop(0)
        if l.startswith('addx'):
            i = (c + 1, int(l.split(' ')[1]))
    if c % 40 == 20:
        t += c * x
    if i and i[0] == c:
        x += i[1]
        i = None
print(t)

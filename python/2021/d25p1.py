from utils import str_list


def move_right(g):
    o = [l[:] for l in g]
    for i,l in enumerate(g):
        for j,x in enumerate(l):
            if x == '>':
                ll = len(l)
                jj = (j + 1) % ll
                if l[jj] == '.':
                    o[i][jj] = x
                    o[i][j] = '.'
    return o

def move_down(g):
    o = [l[:] for l in g]
    for i,l in enumerate(g):
        for j,x in enumerate(l):
            if x == 'v':
                ll = len(g)
                ii = (i + 1) % ll
                if g[ii][j] == '.':
                    o[ii][j] = x
                    o[i][j] = '.'
    return o

def move(g):
    r = move_right(g)
    r = move_down(r)
    return r

g = [list(s) for s in str_list(25)]
n = 0
while True:
    n += 1
    r = move(g)
    if r == g:
        break
    g = r

print(n)

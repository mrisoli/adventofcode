def mov(a, d, x):
    a[d] += x

with open('puzzle.in', 'r') as f:
    r = [0,0]
    s = [0,0]
    v = {tuple(r)}
    turn = 's'
    for c in f.read():
        a = s if turn == 's' else r
        d = 0 if c == '>' or c == '<' else 1
        x = 1 if c == '>' or c == 'v' else -1
        mov(a, d, x)
        v.add(tuple(a))
        turn = 'r' if turn == 's' else 's'
    print(len(v))

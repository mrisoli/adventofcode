with open('puzzle.in', 'r') as f:
    n = [0,0]
    v = {tuple(n)}
    for c in f.read():
        s = 1 if c == '>' or c == 'v' else -1
        d = 0 if c == '>' or c == '<' else 1
        n[d] += s
        v.add(tuple(n))
    print(len(v))

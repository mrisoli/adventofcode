from d17 import run, Vertex, Graph

def neighbours(g: Graph, u: Vertex) -> [Vertex]:
    p, s = u
    ss = 1 if isinstance(s, complex) else 1j
    ss = [ss, -ss]
    t = [(p + si, si) for si in ss if p + si in g]
    if 0 < abs(s.real + s.imag) < 3:
        c = s / abs(s.real + s.imag)
        if p + c in g:
            sp = s + c
            t += [(p + c, s + c)]
    return t

print(run(neighbours))

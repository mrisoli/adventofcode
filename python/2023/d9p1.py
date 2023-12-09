from d9 import gen, solve

def seq(r):
    if set(r) == {0}:
        return r[-1]
    return r[-1] + seq(gen(r))

print(solve(seq))

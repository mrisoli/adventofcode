from utils import coords

DIRECTIONS = [1+1j, -1+1j, -1-1j, 1-1j]
CHECK = ['MMSS', 'SSMM', 'MSSM', 'SMMS']
g = coords(4)

def parse(k):
    return ''.join(g.get(k + v, '.') for v in DIRECTIONS) in CHECK

print(sum(parse(k) for k,v in g.items() if v == 'A'))

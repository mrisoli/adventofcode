from itertools import groupby
with open('puzzle.in', 'r') as f:
    print(sum(len(set(''.join(g))) for k,g in groupby(f.read().splitlines(), key=lambda x: x != '') if k))

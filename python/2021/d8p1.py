from utils import fopen

print(sum([len(list(filter(lambda w: len(w) in [2,3,4,7], x.split(' ')))) for x in [f.split('|')[1].strip() for f in fopen(8).readlines()]]))

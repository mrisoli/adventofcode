from d4 import generate

cards = generate()
d = dict({(c,1) for c in cards.keys()})
for k,v in cards.items():
    for i in range(v):
        d[k + i + 1] += d[k]
print(sum(d.values()))

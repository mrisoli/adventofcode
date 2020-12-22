from common import deck
f = open('p.in').readlines()
p1,p2 = deck.get_hands(f)

while p1 and p2:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2:
        p1 += [c1,c2]
    else:
        p2 += [c2,c1]
print(deck.score(p1,p2))

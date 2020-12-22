from common import deck
f = open('p.in').readlines()
p1,p2 = deck.get_hands(f)

def subgame(h1, h2):
    hands = set()
    while h1 and h2:
        in1 = tuple(h1)
        in2 = tuple(h2)
        hands.update([(in1, in2)])
        run(h1,h2)
        if (tuple(h1),tuple(h2)) in hands:
            return True
    return not(len(h2))

def play(c1, c2, h1, h2):
    if c1 > len(h1) or c2 > len(h2):
        return c1 > c2
    return subgame(h1[:c1],h2[:c2])

def run(ph1, ph2):
    c1 = ph1.pop(0)
    c2 = ph2.pop(0)
    if play(c1, c2, ph1, ph2):
        ph1 += [c1,c2]
    else:
        ph2 += [c2,c1]

while p1 and p2:
    run(p1, p2)
print(deck.score(p1,p2))

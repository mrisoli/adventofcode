from collections import Counter
from utils import str_list
from functools import cmp_to_key

CARD_ORDER = '23456789TJQKA'
JOKER_ORDER = 'J23456789TQKA'

class Hand:
    def __init__(self, hv):
        h, v = hv.split(' ')
        self.cards, self.v = h, int(v)

    def joker_hand(self):
        h = self.cards
        c = Counter([c for c in h if c != 'J'])
        mc = c.most_common(1)
        if len(mc) == 0:
            return Counter(h)
        return Counter(h.replace('J', mc[0][0]))

    def hand_rank(self, jokers):
        c = self.joker_hand() if jokers else Counter(self.cards)
        v = c.values()
        if 5 in v:
            return 6
        elif 4 in v:
            return 5
        elif 3 in v and 2 in v:
            return 4
        elif 3 in v:
            return 3
        elif list(v).count(2) == 2:
            return 2
        elif 2 in v:
            return 1
        else:
            return 0

    def tiebreak(self,b, jokers):
        order = JOKER_ORDER if jokers else CARD_ORDER
        for ca,cb in zip(self.cards, b.cards):
            if order.index(ca) != order.index(cb):
                return order.index(ca) - order.index(cb)
        return 0

class CamelCards:
    def __init__(self, jokers=False):
        self.jokers = jokers
        self.hands = [*map(Hand, str_list(7))]


    def play(self):
        self.hands = sorted(self.hands, key=cmp_to_key(self.rank))

    def winnings(self):
        return sum([h.v * (i + 1) for i,h in enumerate(self.hands)])

    def rank(self, a, b):
        ra = a.hand_rank(self.jokers)
        rb = b.hand_rank(self.jokers)
        if ra != rb:
            return ra - rb
        else:
            return a.tiebreak(b, self.jokers)

from utils import fopen

class Card:
    def __init__(self, rows):
        self.numbers = self.make_numbers(rows)
        self.hits = { 'r': [0] * 5, 'c': [0] * 5 }

    def make_numbers(self, rows):
        n = {}
        for r in range(len(rows)):
            for c in range(len(rows[r])):
                n[rows[r][c]] = (r, c)
        return n

    def mark(self, number):
        if number in self.numbers:
            (r,c) = self.numbers[number]
            del self.numbers[number]
            self.hits['r'][r] += 1
            self.hits['c'][c] += 1
            if self.hits['r'][r] == 5 or self.hits['c'][c] == 5:
                return True
        return False

    def calc(self, v):
        return v * sum(map(int, self.numbers.keys()))

class Board:
    def __init__(self, cards):
        self.cards = self.make_cards(cards)
        self.boards = [{}] * len(cards)

    def make_cards(self, cards):
        b = {}
        for i in range(len(cards)):
            c = cards[i]
            b[i] = Card(c)
        return b

    def mark_cards(self, n):
        l = []
        for i,card in self.cards.items():
            if card.mark(n):
                l.append(i)
        if len(l) > 0:
            for i,card in enumerate(l):
                del self.cards[i]
            return card
        return None

    def is_last_winner(self):
        return len(self.cards) == 0

def solve(first=True):
    f = fopen(4)

    draw, _, *numbers = f.readlines()

    cards = [[]]
    card_index = 0
    for r in numbers:
        if r == '\n':
            cards.append([])
            card_index += 1
            continue
        cards[card_index].append(r.strip().split())

    board = Board(cards)
    for d in draw.split(','):
        winner = board.mark_cards(d)
        if winner and (first or board.is_last_winner()):
            print(winner.calc(int(d)))
            break

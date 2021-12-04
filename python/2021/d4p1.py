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
        return v * sum([int(n) for n in self.numbers.keys()])

class Board:
    def __init__(self, cards):
        self.cards = [Card(c) for c in cards]
        self.boards = [{}] * len(cards)

    def mark_cards(self, n):
        for card in self.cards:
            if card.mark(n):
                return card
        return None

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
    if winner:
        print(winner.calc(int(d)))
        break

from common import seat

with open('puzzle.in') as f:
    l = [seat.get_seat(s) for s in f.read().splitlines()]
    print(max(set(range(max(l))) - set(l)))

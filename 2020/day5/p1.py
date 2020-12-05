from common import seat
with open('puzzle.in') as f:
    print(max([seat.get_seat(s) for s in f.read().splitlines()]))

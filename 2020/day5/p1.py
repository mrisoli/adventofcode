from common import seat
with open('puzzle.in') as f:
    print(max(map(seat.get_seat, f.read().splitlines())))

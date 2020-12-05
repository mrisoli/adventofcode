from common import seat

def find_missing(seats):
    m = max(seats)
    s = set(seats)
    for i in range(m):
        if i not in s and i - 1 in s and i + 1 in s:
            return i

with open('puzzle.in') as f:
    print(find_missing([seat.get_seat(s) for s in f.read().splitlines()]))

from utils import int_row

l = int_row(7)
print(min([sum([sum(range(abs(x - y) + 1)) for y in l]) for x in l]))

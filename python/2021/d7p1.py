from utils import int_row

l = int_row(7)
print(min([sum([abs(x - y) for y in l]) for x in l]))

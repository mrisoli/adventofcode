from utils import rows_of_int
print(sum(abs(r - l) for l, r in zip(*map(sorted, zip(*rows_of_int(1))))))

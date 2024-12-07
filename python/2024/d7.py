from utils import rows_of_int

class TestChecker:
    def __init__(self, concat=False):
        self.f = rows_of_int(7)
        self.concat = concat

    def verify(self, value, operators, acc):
        if operators == []:
            return acc == value
        if acc > value:
            return False
        current, *ops = operators
        return self.verify(value, ops, acc + current) or self.verify(value, ops, acc * current) or (self.concat and self.verify(value, ops, int(str(acc) + str(current))))

    def check(self, l):
        [value, first_operator, *operators] = l
        return value if self.verify(value, operators, first_operator) else 0

    def solve(self):
        return sum(map(self.check, self.f))

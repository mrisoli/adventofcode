from math import prod
from d8 import Point,Grid

class PointSight(Point):
    def sight(self):
        return prod(self.get_predicates())

    def checkfn(self, rn):
        t = 0
        for v1 in rn:
            t += 1
            if self.get() <= v1:
                break
        return t

g = Grid()
print(max([PointSight(g, i, j).sight() for (i, j) in g.yield_points()]))

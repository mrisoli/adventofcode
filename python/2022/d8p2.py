from math import prod
from utils import fopen
from d8 import Point,get_grid, yield_points

class PointSight(Point):
    def sight(self):
        return prod([self.top(), self.bottom(), self.right(), self.left()])

    def checkfn(self, rn):
        t = 0
        for v1 in rn:
            t += 1
            if self.get() <= v1:
                break
        return t

g = get_grid()
print(max([PointSight(g, i, j).sight() for (i, j) in yield_points(g)]))

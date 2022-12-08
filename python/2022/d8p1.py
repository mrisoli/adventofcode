from utils import fopen
from d8 import Point, get_grid, yield_points

g = get_grid()

class PointVis(Point):
    def visible(self):
        return self.top() or self.right() or self.bottom() or self.left()

    def checkfn(self, rn):
        return all(map(lambda v1: self.get() > v1, rn))

print((4 * len(g)) - 4 + len([1 for (i,j) in yield_points(g) if PointVis(g, i, j).visible()]))

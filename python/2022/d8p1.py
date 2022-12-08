from d8 import Point, Grid

g = Grid()

class PointVis(Point):
    def visible(self):
        return any(self.get_predicates())

    def checkfn(self, rn):
        return all(map(lambda v1: self.get(self.i, self.j) > v1, rn))

print((4 * g.len) - 4 + sum(filter(bool, [PointVis(g, i, j).visible() for i,j in g.yield_points()])))

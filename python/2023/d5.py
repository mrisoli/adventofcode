from operator import itemgetter
from utils import obj_list

ORDER = ['soil', 'fertilizer', 'water', 'light', 'temperature','humidity', 'location']

class Pairing:
    def __init__(self, ranges):
        self.destination, self.source, self.rn = ranges
        self.interval = (self.destination, self.source, self.rn)

    def source_range(self):
        return self.source, self.source + self.rn

    def destination_range(self):
        return self.destination, self.destination + self.rn

    def offset(self):
        return self.destination - self.source

    def get_leftover(self, x, y):
        leftover = []
        min_x, max_x = x
        min_y, max_y = y
        los = [(min_x, min_y), (max_y, max_x)]
        return set(a for a in los if a[0] < a[1])

    def get_intersection(self, x):
        solutions = []
        min_x, max_x = x
        min_y, max_y = self.source_range()
        match = (max(min_x,min_y), min(max_x, max_y))
        solution = self.transform(match) if match[0] < match[1] else None
        leftover = self.get_leftover(x, match) if solution else set([x])
        return solution, leftover

    def transform(self, rng):
        o = self.offset()
        return (rng[0] + o, rng[1] + o)

class Maps:
    def __init__(self, m, seeds, rn):
        self.mappings = self.parse_maps(m)
        self.mappings['seed'] = self.gen_seeds(seeds, rn)

    def seed_pair(self, seed, length):
        return Pairing((seed, seed, length))

    def gen_seeds(self, seeds, rn):
        iseeds = [*map(int, seeds)]
        pairs = zip(iseeds[0::2], iseeds[1::2])
        if rn:
            pairs = zip(iseeds[0::2], iseeds[1::2])
            return [self.seed_pair(s, l) for s,l in pairs]
        return [*map(lambda i: self.seed_pair(i, 1), iseeds)]

    def split_paths(self, path):
        return map(int, path.split(' '))

    def get_values(self, paths):
        return [*map(Pairing, map(self.split_paths, paths))]

    def get_map(self, m):
        name, *paths = m.split('\n')
        name = (name.split()[0]).split('-to-')[1]
        return name, self.get_values(paths)

    def parse_maps(self, m):
        return dict(map(self.get_map, m))

    def get_ranges(self, name):
        return self.mappings[name]

class PathFinder:
    def __init__(self, maps):
        self.maps = maps

    def parse_seeds(self):
        paths = set(map(Pairing.source_range, self.maps.get_ranges('seed')))
        for source in ORDER:
            matches = set()
            for r in self.maps.get_ranges(source):
                new_paths = set()
                for c in paths:
                    sl,lo = r.get_intersection(c)
                    if sl:
                        matches.add(sl)
                    new_paths = new_paths.union(lo)
                paths = new_paths
            paths = matches.union(new_paths)
        return paths

class LocationFinder:
    def __init__(self, rn=None):
        seeds, *maps = obj_list(5)
        self.path = PathFinder(Maps(maps, seeds.split(' ')[1:], rn))

    def get_location(self):
        return min(map(itemgetter(0), self.path.parse_seeds()))

from operator import itemgetter
from utils import obj_list

ORDER = ['soil', 'fertilizer', 'water', 'light', 'temperature','humidity', 'location']

class Pairing:
    def __init__(self, destination, source, rn):
        self.destination = destination
        self.source = source
        self.rn = rn

    def contains(self, value):
        return value in range(self.source, self.source + self.rn)

    def offset(self, value):
        offset = value - self.source
        return self.destination + offset


class Maps:
    def __init__(self, m):
        self.paths = self.parse_maps(m)

    def pairings(self, path):
        destination, source, rn = map(int, path.split(' '))
        return Pairing(destination, source, rn)

    def get_values(self, paths):
        return [*map(self.pairings, paths)]

    def get_map(self, m):
        name, *paths = m.split('\n')
        name = (name.split()[0]).split('-to-')[1]
        return name, self.get_values(paths)

    def parse_maps(self, m):
        return dict(map(self.get_map, m))

    def get_ranges(self, name):
        return self.paths[name]

class LocationFinder:
    def __init__(self, rn=1):
        seeds, *maps = obj_list(5)
        seeding = seeds.split(' ')[1:]
        self.seeds = dict([(int(i), {}) for i in seeding])
        self.maps = Maps(maps)

    def parse_seeds(self):
        for n,seed in self.seeds.items():
            c = n
            for name in ORDER:
                for pl in self.maps.get_ranges(name):
                    if pl.contains(c):
                        c = pl.offset(c)
                        self.seeds[n][name] = c
                        break
                if name not in self.seeds[n]:
                    self.seeds[n][name] = c


    def get_location(self):
        self.parse_seeds()
        return min(map(itemgetter('location'), self.seeds.values()))

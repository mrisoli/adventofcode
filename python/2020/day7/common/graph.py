import re

vp = re.compile(r'(?P<v>\w+\s\w+) bags contain')
ep = re.compile(r'(?P<bags>\d+)\s(?P<color>\w+\s\w+)\sbags?(,\s)?')

class Vertex:
    def __init__(self, name, edges):
        self.edges = dict()
        self.name = name
        for e in edges:
            bags = int(e['bags'])
            self.edges[e['color']] = {'bags': bags, 'color': e['color']}

    def get_edge_names(self):
        return list(self.edges.keys())

    def get_bags_sum(self):
        return sum([self.edges[e]['bags'] for e in self.edges])

class Graph:
    def __init__(self, l):
        self.vertices = dict()
        for s in l:
            name = re.match(vp, s).group('v')
            edges = [er.groupdict() for er in re.finditer(ep, s)]
            self.vertices[name] = Vertex(name, edges)

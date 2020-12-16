from common import graph

def count_bags(g, color):
    v = g.vertices[color]
    c = v.get_bags_sum()
    for name in v.edges:
        n = g.vertices[color].edges[name]['bags']
        c += (n * g.count_bags(name))
    return c

with open('puzzle.in', 'r') as f:
    g = graph.Graph(f.read().splitlines())
    print(count_bags(g, 'shiny gold'))

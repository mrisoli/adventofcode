from common import graph
with open('puzzle.in', 'r') as f:
    g = graph.Graph(f.read().splitlines())
    print(g.count_colors('shiny gold'))

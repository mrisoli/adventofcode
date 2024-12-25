from utils import points_list
from coordinates import dijkstra

f = points_list(18)
mx = int(max(map(lambda x: x.real, f)))
my = int(max(map(lambda y: y.imag, f)))
start = 0
end = mx + my * 1j
for i in range(len(f)):
    ff = f[:i]
    shortest_path_length = dijkstra((mx, my), ff, start, end)
    if shortest_path_length is None:
        print(f[i-1])
        break

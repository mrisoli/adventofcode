from utils import rows_of_int
from itertools import combinations

reds =  rows_of_int(9)
reds = [complex(*t) for t in reds]

def get_largest_rect_area(vertices):
    n = len(vertices)
    max_area = 0

    def is_point_inside(p):
        inside = False
        for k in range(n):
            v1, v2 = vertices[k], vertices[(k + 1) % n]
            if ((v1.imag > p.imag) != (v2.imag > p.imag)):
                intersect_x = (v2.real - v1.real) * (p.imag - v1.imag) / (v2.imag - v1.imag) + v1.real
                if p.real < intersect_x:
                    inside = not inside
        return inside

    def edge_cuts_rectangle(x_min, x_max, y_min, y_max):
        for k in range(n):
            v1, v2 = vertices[k], vertices[(k + 1) % n]

            if v1.real == v2.real:
                if x_min < v1.real < x_max:
                    ev_min, ev_max = sorted((v1.imag, v2.imag))
                    if max(y_min, ev_min) < min(y_max, ev_max):
                        return True

            else:
                if y_min < v1.imag < y_max:
                    ev_min, ev_max = sorted((v1.real, v2.real))
                    if max(x_min, ev_min) < min(x_max, ev_max):
                        return True
        return False

    for i in range(n):
        for j in range(i + 1, n):
            r1, r2 = vertices[i], vertices[j]

            min_x, max_x = sorted((r1.real, r2.real))
            min_y, max_y = sorted((r1.imag, r2.imag))

            current_area = (max_x - min_x + 1) * (max_y - min_y + 1)
            if current_area <= max_area:
                continue

            center = complex((min_x + max_x) / 2, (min_y + max_y) / 2)
            if not is_point_inside(center):
                continue

            if edge_cuts_rectangle(min_x, max_x, min_y, max_y):
                continue

            max_area = current_area

    return max_area

result = get_largest_rect_area(reds)
print(result)

from itertools import combinations
from math import dist
from utils import rows_of_int

def distances(points):
    return sorted(
            [
                {
                    "d": dist(points[i], points[j]),
                    "points": (i, j)
                    }
                for i, j in combinations(range(len(points)), 2)
                ],
            key=lambda x: x["d"]
            )

def get_x(points, point):
    return points[point][0]

def connect_all(points):
    d = distances(points)
    boxes = set(range(len(points)))
    circuits = []

    for p in d:
        point_a, point_b = p['points']

        # Check which circuits contain point_a or point_b
        circuit_a = None
        circuit_b = None

        # We iterate over a copy or by index because we might modify 'circuits'
        for circuit in circuits:
            if point_a in circuit:
                circuit_a = circuit
            if point_b in circuit:
                circuit_b = circuit

        # CASE 1: Both points are brand new (start a new circuit)
        if circuit_a is None and circuit_b is None:
            circuits.append({point_a, point_b})
            if point_a in boxes: boxes.remove(point_a)
            if point_b in boxes: boxes.remove(point_b)

        # CASE 2: Only point A is in a circuit (add B to A's circuit)
        elif circuit_a is not None and circuit_b is None:
            circuit_a.add(point_b)
            if point_b in boxes: boxes.remove(point_b)

        # CASE 3: Only point B is in a circuit (add A to B's circuit)
        elif circuit_b is not None and circuit_a is None:
            circuit_b.add(point_a)
            if point_a in boxes: boxes.remove(point_a)

        # CASE 4: Both are in circuits
        else:
            # If they are in DIFFERENT circuits, merge them
            if circuit_a is not circuit_b:
                # Merge b into a
                circuit_a.update(circuit_b)
                # Remove the old separate circuit b
                circuits.remove(circuit_b)
            # If they are in the SAME circuit, do nothing (connection already exists)
        if len(boxes) == 0 and len(circuits) == 1:
            ax = get_x(points, point_a)
            bx = get_x(points, point_b)
            print(ax, bx)
            return ax * bx

f = list(map(tuple, rows_of_int(8)))
print(connect_all(f))

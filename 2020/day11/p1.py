from common import seat

def neighbours(m, i, j):
    o = 0
    for ni in [-1, 0, 1]:
        for nj in [-1, 0, 1]:
            nii = i + ni
            njj = j + nj
            if nii == i and njj == j:
                continue
            if 0 <= nii < len(m) and 0 <= njj < len(m[i]) and m[nii][njj] == '#':
                o += 1
    return o

seat.solve_with(4, neighbours)
